
from requests import get
from secrets import API_KEY
import json

BASE_URL = "https://free.currconv.com/"


headers = {
    "accept": "application/json"
}

def get_currencies():
    end_point = f"api/v7/currencies?apiKey={API_KEY}"
    search_url = BASE_URL + end_point

    
    response = get(search_url, headers = headers)
    data = response.json()['results']
    data = list(data.items())
    data.sort()
    return data


def rate_value(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id_ = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id_} - {name} - {symbol}")
        

def getSymbol(currencies, current_currency):
    for symbol, currency in currencies:
        currencyid = currency['id']
        if currencyid == current_currency.upper():
            symbol = currency.get("currencySymbol", "&")
            return symbol
       
         
def exchange_rate(currency1, currency2):
    end_point = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    search_url = BASE_URL + end_point
    data = get(search_url).json()
    

    if len(data) == 0:
        print("Invalid currency ID, please check and try again!")
        return len(data)

    rate = list(data.values())[0]
    print(f"\nThe exchange rate of One {currency1} is equal to {rate} {currency2}\n")
    return rate


def converts(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    
    if rate == 0:
        return 
    try:
        amount = float(amount)
        
    except:
        print("Invalid amount entered, please check and enter a valid amount!")
        return

    amt_converted = float(amount * rate)
    print(f"{amount} {currency1} is equal to {amt_converted} {currency2}\n")
    return amt_converted


def currencies_exchange():
    currencies = get_currencies()


    print(f"\n............Welcome To Currency Converter.............!")
    
    while True:
        print("---------------------------------------------------------------------------------------------------")
        print("\nEnter '1' to list all the differnt currencies")
        print("\nEnter '2' to convert from one currency to another")
        print("\nEnter '3' to get the exchange rate of your currency's")
        print("\nEnter 'q' to quit......................................!")
        print("---------------------------------------------------------------------------------------------------")

        
        command = input("\nPlease enter a command to continue, or ('q' to quit):\n\n")
        if command == "q":
            print("\nThank you for using currency converter!")
            break

        elif command == "1":
            print("\nThese are all the currencies you can convert......!\n\n")
            rate_value(currencies)
            
    
        elif command == "2":
            currency1 = input("\nPlease enter the first curreny id:\n\n").upper()
            currency2 = input("\nPlease the enter the second curreny id:\n\n").upper()
            amount = input(f"\nPlease enter the amount in currency1:\n\n{getSymbol(currencies, currency1)}")
            converts(currency1, currency2, amount)
          
              
        
        elif command == "3":
            currency1 = input("\nPlease enter your first curreny id:\n\n").upper()
            currency2 = input("\nPlease the enter your second curreny id:\n\n").upper()
            exchange_rate(currency1, currency2)

        else:
            print("Invalid command")
currencies_exchange()

