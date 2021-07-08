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
                (3) -- View data analytics
                (4) -- Clear history
                (0) -- Quit
                Enter choice: """)

            if choice == '1':
                self.fact_menu()

            elif choice == '2':
                self.history_menu()

            elif choice == '3':
                self.data_menu()

            elif choice == '4':
                self.dbinter.deleteDB('math_bites')
                self.dbinter.createDB('math_bites')

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
                (2) -- Trivia fact ('random' for a random fact!)
                (3) -- Year fact
                (4) -- Date fact
                (5) -- Text fact (EXPERIMENTAL!)
                (0) -- Return to main menu
                Enter choice: """)

            if choice == '1':
                entry = input("What number would you like to look up? ")
                self.math_lookup(entry)

            elif choice == '2':
                entry = input("What number would you like to look up? ")
                self.trivia_lookup(entry)

            elif choice == '3':
                entry = input("What year would you like to look up? ")
                self.year_lookup(entry)

            elif choice == '4':
                entry_month = input(
                    "What month would you like to look up? (Numerical) ")
                entry_day = input(
                    "What day would you like to look up? (Numerical) ")

                self.date_lookup(entry_day, entry_month)

            elif choice == '5':
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
        self.dbinter.addEntry('main', number)

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
        self.dbinter.addEntry('main', number)

    def date_lookup(self, day, month):
        url = ("https://numbersapi.p.rapidapi.com/" +
               month +
               "/" +
               day +
               "/date")

        response_data = self.get_data(url).json()

        print("On {}/{}/{}, the {} day of the year, {}."
              .format(month,
                      day,
                      response_data['year'],
                      response_data['number'],
                      response_data['text']))

        self.dbinter.addEntry('date', '{}'.format(response_data['number']))
        self.dbinter.addEntry('main', '{}'.format(response_data['number']))

    def get_data(self, url):
        QUERYSTRING = {"json": "true", "fragment": "true"}
        HEADERS = {
            'x-rapidapi-key': self.KEY,
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

        return requests.request("GET",
                                url,
                                headers=HEADERS,
                                params=QUERYSTRING)

    def history_menu(self):
        while True:
            choice = input("""
                What search history would you like to see?
                (1) -- Main history
                (2) -- Math history
                (3) -- Trivia history
                (4) -- Year history
                (5) -- Date history
                (0) -- Return to main menu
                Enter choice: """)

            if choice == '1':
                self.dbinter.showTable('main')

            elif choice == '2':
                self.dbinter.showTable('math')

            elif choice == '3':
                self.dbinter.showTable('trivia')

            elif choice == '4':
                self.dbinter.showTable('year')

            elif choice == '5':
                self.dbinter.showTable('date')

            elif choice == '0':
                break

            else:
                print("Invalid input! ")

    def data_menu(self):
        while True:
            choice = input("""
                What information would you like displayed?
                (1) -- Mathematics
                (2) -- Trivia
                (3) -- Year
                (4) -- Date
                (0) -- Return to previous menu
                Enter choice: """)

            if choice == '1':
                self.dbinter.showScatter('math')

            elif choice == '2':
                self.dbinter.showScatter('trivia')

            elif choice == '3':
                self.dbinter.showScatter('year')

            elif choice == '4':
                self.dbinter.showScatter('date')

            elif choice == '0':
                break

            else:
                print("Invalid input! ")


if __name__ == "__main__":
    main = MathBites()
    main.main_menu()
