# Import necessary modules
import requests
from DB_Func import DB_Func

class MathBites:
    def __init__(self):
        self.KEY = "8ea42e22ddmsh636295d97820b16p13f8fajsn0f1762f562d0"
        self.dbinter = DB_Func()
        self.dbinter.createDB('math_bites')
    
    def main_menu(self):
        while True:
            choice = input("""
                What would you like to do?
                (1) -- Look up a fact 
                (2) -- View previous searches
                (0) -- Quit
                Enter choice: """)

            if choice == '1':
                self.fact_menu()

            elif choice == '2':
                self.history_menu()

            elif choice == '0':
                print("Bye!")
                break

            else:
                print("Invalid input! ")


    def fact_menu(self):
        while True:
            choice = input("""
                What kind of fact would you like to look up?
                (1) -- Math fact
                (2) -- Trivia fact
                (3) -- Random fact
                (4) -- Year fact
                (5) -- Date fact
                (6) -- Text fact (EXPERIMENTAL!)
                (0) -- Return to main menu
                Enter choice: """)

            if choice == '1':
                entry = input("What number would you like to look up? ")
                self.math_lookup(entry)

            elif choice == '2':
                entry = input("What number would you like to look up? ")
                self.trivia_lookup(entry)

            elif choice == '3':
                self.trivia_lookup('random')

            elif choice == '4':
                entry = input("What year would you like to look up? ")
                self.year_lookup(entry)

            elif choice == '5':
                entry_month = input(
                    "What month would you like to look up? (Please enter number) ")
                entry_day = input(
                    "What day would you like to look up? (Please enter number) ")
                self.date_lookup(entry_day, entry_month)

            elif choice == '6':
                entry = input("What text would you like to look up? ")

                text_num = 0

                for letter in entry:
                    text_num += ord(letter)

                self.math_lookup(str(text_num))

            elif choice == '0':
                break

            else:
                print("Invalid input! ")


    def math_lookup(self, number):
        url = "https://numbersapi.p.rapidapi.com/" + number + "/math"
        response_data = self.get_data(url).json()

        print("{} is {}.".format(response_data['number'],
                                 response_data['text']))
        self.dbinter.addEntry('math', number)


    def trivia_lookup(self, number):
        url = "https://numbersapi.p.rapidapi.com/" + number + "/trivia"
        response_data = self.get_data(url).json()

        print("{} is {}.".format(response_data['number'],
                                 response_data['text']))
        self.dbinter.addEntry('trivia', number)


    def year_lookup(self, number):
        url = "https://numbersapi.p.rapidapi.com/" + number + "/year"
        response_data = self.get_data(url).json()

        print("{} is the year {}.".format(response_data['number'],
                                          response_data['text']))
        self.dbinter.addEntry('year', number)
        

    def date_lookup(self, day, month):
        url = "https://numbersapi.p.rapidapi.com/" + month + "/" + day + "/date"
        response_data = self.get_data(url).json()
        
        print("On {}/{}/{}, {}.".format(month,
                                        day,
                                        response_data['year'],
                                        response_data['text']))
        self.dbinter.addEntry('date', '{}/{}'.format(month, day))


    def get_data(self, url):
        QUERYSTRING = {"json": "true", "fragment": "true"}
        HEADERS = {
            'x-rapidapi-key': self.KEY,
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

        return requests.request("GET", url, headers=HEADERS, params=QUERYSTRING)


    def history_menu(self):
        while True:
            choice = input("""
                What search history would you like to see?
                (1) -- Math history
                (2) -- Trivia history
                (3) -- Year history
                (4) -- Date history
                (0) -- Return to main menu
                Enter choice: """)

            if choice == '1':
                self.dbinter.showTable('math')

            elif choice == '2':
                self.dbinter.showTable('trivia')

            elif choice == '3':
                self.dbinter.showTable('year')

            elif choice == '4':
                self.dbinter.showTable('date')

            elif choice == '0':
                break

            else:
                print("Invalid input! ")


if __name__ == "__main__":
    main = MathBites()
    main.main_menu()
