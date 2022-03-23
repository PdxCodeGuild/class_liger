"""
Lab 10

version 1 

"""


import requests


BASE_URL = "https://icanhazdadjoke.com/"

headers = {"accept": "application/json"}


response = requests.get(BASE_URL, headers=headers)
data = response.json()

print("\n>>> Here's a dad joke for you; enjoy...")


USER_CHOICE = "y"
while USER_CHOICE == "y":
    response = requests.get(BASE_URL, headers=headers)
    # USER_CHOICE == "n"
    data = response.json()
    print(f'\n\t{data["joke"]}\n')
    USER_CHOICE = input(">>> A real knee-slapper! Would you like another? [y/n]: ")

print("\nTo borrow a line from 'NSYNC: Bye, Bye, Bye!")
