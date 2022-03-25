"""
Lab 10

versions 1 & 2 

"""

import requests


def version_1():
    base_url = "https://icanhazdadjoke.com/"

    headers = {"accept": "application/json"}

    response = requests.get(base_url, headers=headers)
    data = response.json()

    print("\n>>> Here's a dad joke for you; enjoy...")

    user_choice = "y"
    while user_choice == "y":
        response = requests.get(base_url, headers=headers)
        data = response.json()
        your_joke = f'\n\t{data["joke"]}\n'
        print(your_joke)
        user_choice = input(">>> A real knee-slapper! Would you like another? [y/n]: ")

    print("\nTo borrow a line from 'NSYNC: Bye, Bye, Bye!")


# version_1()

""" version 2"""

base_url = "https://icanhazdadjoke.com/"

headers = {"accept": "application/json"}
activity_choices = "js"

page_selection = ""
activity_selection = input("Enter 'j' for a random dad Joke or 's' to Search for joke topics\n>>> [j/s] ").lower()

while activity_selection not in activity_choices:
    print("\n\tInvalid input!\n")
    activity_selection = input("Only enter 'j' for a random dad Joke or 's' to Search joke topics\n>>> [j/s] ").lower()

if activity_selection == "j":

    response = requests.get(base_url, headers=headers)
    data = response.json()

    print("\n>>> Here's a dad joke for you; enjoy...")

    user_choice = "y"
    while user_choice == "y":
        response = requests.get(base_url, headers=headers)
        data = response.json()
        print(f'\n\t{data["joke"]}\n')
        user_choice = input("A real knee-slapper! Would you like another?\n>>> [y/n] ")

    print("\nTo borrow from 'NSYNC: Bye, Bye, Bye!")

else:

    term = input("\nEnter the subject to search for (e.g. dog)\n>>> ").lower()
    params_dict = {"page": page_selection, "term": term}
    response = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params_dict)
    data = response.json()
    limit = data["limit"]
    number_of_jokes = data["total_jokes"]
    number_of_pages = data["total_pages"]
    print(f"\nThis search returned: {number_of_jokes} joke(s) on {number_of_pages} page(s)\n")
    results = data["results"]

    while number_of_jokes == 0:
        print("The joke's on you! No results returned; please try again.\n")
        term = input("Enter the subject to search for (e.g. dog)\n>>> ").lower()
        params_dict = {"page": page_selection, "term": term}
        response = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params_dict)
        data = response.json()
        limit = data["limit"]
        number_of_jokes = data["total_jokes"]
        number_of_pages = data["total_pages"]
        print(f"\nThis search returned: {number_of_jokes} joke(s) on {number_of_pages} page(s)")
        results = data["results"]

    jokes_viewed = []
    user_choice = "y"
    while user_choice == "y":
        if number_of_pages > 1:
            page_selection = input(
                f"Enter a number from 1 to {number_of_pages} to read the jokes on the desired page\n>>> "
            )
            params_dict = {"page": page_selection, "term": term}
            response = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params_dict)
            data = response.json()
            limit = data["limit"]
            if int(page_selection) > 1:
                number_of_jokes = data["total_jokes"] - limit
                number_of_pages = data["total_pages"]
                print(f"This search returned: {number_of_jokes} jokes on {number_of_pages} page(s)\n")
                results = data["results"]
            else:
                number_of_jokes = limit
                results = data["results"]
        selection = input(
            f"\nEnter a number from 1 to {number_of_jokes} to read the joke(s) on page {page_selection}\n>>> "
        )
        selection = int(selection)
        jokes_viewed.append(selection)
        joke_index = selection - 1
        print(f'\n{results[joke_index]["joke"]}')
        user_choice = input(f"\nYou've seen joke #(s) {jokes_viewed}; would you like another?\n>>> [y/n] ")

    print("\nTo borrow from 'NSYNC: Bye, Bye, Bye!")
