import requests

def display_menu(menu):
    for key in menu.keys():
        print(f"{key}. {menu[key]}")

BASE_URL = "https://swapi.dev/api"

FILMS_URL = BASE_URL + '/films'
PEOPLE_URL = BASE_URL + '/people'

# tells the API to return JSON data in the response instead of HTML/CSS
headers = {
    'Accept': 'application/json'
}

# the '?term=string' is a url parameter
# term is the key, a string will be provided as the value
# SEARCH_URL = f"https://icanhazdadjoke.com/search?term={term}"

menu = {
    '1': 'People',
    '2': 'Films'
}

print("Welcome to the Star Wars library!")
while True:
    print("\nPlease choose one of the following options to search: ")
    
    display_menu(menu)

    option = input("\nEnter your selection:\n> ")
    while not menu.get(option):
        print("Invalid selection!")
        print("\nPlease choose one of the following options to search: ")

        display_menu(menu)

        option = input("\nEnter your selection:\n> ")


    if option == '1':
        # get list of people and display
        pass

    elif option == '2':
        # get list of films and display

        # http get request
        response = requests.get(FILMS_URL) # ***

        # convert json string to python data
        data = response.json() # ***

        # pull the list of results out of the data dictionary
        results = data['results']

        print("Please select a film: ")

        # list the films with numbers (e.g. 1. A New Hope)
        for index, film in enumerate(results):
            print(f"{index + 1}. {film['title']}")

        option = input("\nEnter a film number to see its characters:\n> ")

        option = int(option)
        film_index = option - 1
        film = results[film_index]


        print(f"\nCharacters in {film['title']}:")
        for character_url in film['characters']:
            response = requests.get(character_url) # ***
            character_info = response.json()       # ***

            print(f"- {character_info['name']}")