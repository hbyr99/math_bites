# Import necessary modules
import requests


def fact_menu():
    choice = input("""
        What kind of fact would you like to look up?
        (1) -- Math fact
        (2) -- Trivia fact
        (3) -- Random fact
        (4) -- Year fact
        (5) -- Date fact
        (6) -- Text fact (EXPERIMENTAL!)
        Enter choice: """
    )
    
    if choice == '1':
        entry = input("What number would you like to look up? ")
        math_lookup(entry)
        
        
    elif choice == '2':
        entry = input("What number would you like to look up? ")
        trivia_lookup(entry)
        
        
    elif choice == '3':
        trivia_lookup('random')
        
        
    elif choice == '4':
        entry = input("What year would you like to look up? ")
        year_lookup(entry)
        
    elif choice == '5':
        entry_month = input(
            "What month would you like to look up? (Please enter the month number) ")
        entry_day = input(
            "What day would you like to look up? (Please enter the day number) ")
        date_lookup(entry_day, entry_month)
    
    
    elif choice == '6':
        entry = input("What text would you like to look up? ")
        
        text_num = 0
        
        for letter in entry:
            text_num += ord(letter)
        
        math_lookup(str(text_num))
        
    else:
        menu()

        
def math_lookup(number):
    url = "https://numbersapi.p.rapidapi.com/" + number + "/math"
    response_data = get_data(url).json()
    
    print("{} is {}.".format(response_data['number'], response_data['text']))

    
def trivia_lookup(number):
    url = "https://numbersapi.p.rapidapi.com/" + number + "/trivia"
    response_data = get_data(url).json()
    
    print("{} is {}.".format(response_data['number'], response_data['text']))

    
def year_lookup(number):
    url = "https://numbersapi.p.rapidapi.com/" + number + "/year"
    response_data = get_data(url).json()
    
    print("{} is the year {}.".format(response_data['number'], response_data['text']))


def date_lookup(day, month):
    url = "https://numbersapi.p.rapidapi.com/" + month + "/" + day + "/date"
    response_data = get_data(url).json()
    
    print("On {}/{}/{}, {}.".format(month,
                                    day,
                                    response_data['year'],
                                    response_data['text']))
    

def get_data(url):
    QUERYSTRING = {"json":"true","fragment":"true"}
    HEADERS = {
    'x-rapidapi-key': "8ea42e22ddmsh636295d97820b16p13f8fajsn0f1762f562d0",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }
    
    return requests.request("GET", url, headers=HEADERS, params=QUERYSTRING)


if __name__ == "__main__":
    fact_menu()