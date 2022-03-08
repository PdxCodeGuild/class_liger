import requests

'''
Dictionaries ('dict')

- one of the most powerful datatypes in Python
- can be used to store large amounts of data and make accessing that data quick and easy
- collections of key:value pairs
- keys are used to access values

- are defined using curly brackets {}
- keys and values are separated with colons
- key:value pairs are called 'items'
- items are separated with commas
'''

# blank dictionary
blank_dictionary = {}

[1,2,3] # list
(1,2,3) # tuple - immutable list

# ---------------------------------------------------------------------------- #

# dict keys are generally strings
# dict values can be ANY datatype, including other dictionaries

example_dict = { 'a': 11, 'b': 22, 'c': 33 }

# dicts can be arranged vertically
example_dict = {
    # key: value,
    'a': 11,
    'b': 22,
    'c': 33
}

# dictionary values are retrieved by placing their keys
# in SQUARE brackets after the dictionary's name
# print(example_dict['a']) # 11
# print(example_dict['b']) # 22
# print(example_dict['c']) # 33

# ---------------------------------------------------------------------------- #

# dicts are usually used for grouping related data

# address 1
street = '123 Faux St.'
city = 'Portland'
state = 'Oregon'
zipcode = '123456'

address_1 = {
    'street': '123 Faux St.',
    'city': 'Portland',
    'state': 'Oregon',
    'zipcode': '123456'
}

address_2 = {
    'street': '123 Faux St.',
    'city': 'Portland',
    'state': 'Oregon',
    'zipcode': '123456'
}

# print(address_1['street']) # 123 Faux St.

# -------------------------------------------------------------------------------- #

book = {
    'title': 'The Hobbit',
    'author': 'JRR Tolkein',
    'pages': 200,
    # 'property_1': 'hello world'
}

# print(f"The book {book['title']} was written by {book['author']} and has {book['pages']} pages")

# cannot retrieve values at non-existent keys
# print(book['characters']) # KeyError: 'characters'

# compute the key dynamically and then use it
# ID = 11
# key = f"property_{ID}"
# print(book[key])

# -------------------------------------------------------------------------------------- #

# add a value at the key of 'characters'
book['characters'] = ['Bilbo', 'Gandalf', 'Smaug']
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug']

# retrieve an item from the list at the key of 'characters'
# print(book['characters'][1]) # Gandalf

book['characters'].append('Balin')
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug', 'Balin']

# -------------------------------------------------------------------------------------- #

# change the value at a key
book['pages'] = 199
# print(book['pages']) # 199

# --------------------------------------------------------------------------------------- #

# deleting a key:value pair
# keyword 'del'
# del book['pages']
# print(book['pages']) # KeyError: 'pages'

# --------------------------------------------------------------------------------------- #

# dict methods

# .pop(key) - remove the key:value pair at the key and return the value
pages = book.pop('pages')
# print(pages, book) # 199 {'title': 'The Hobbit', 'author': 'JRR Tolkein', 'characters': ['Bilbo', 'Gandalf', 'Smaug', 'Balin']}

# ---------------------------------------------------------------------------------------- #

# .update(new_dict) - add the items from the new_dict to the original
new_items = {
    'pages': 200,
    'isbn_number': 2983749283749823649826
}

# book.update(new_items)

# adding the items using an anonymous dict
# book.update({
#     'pages': 200,
#     'isbn_numbers': 2983749283749823649826
# })

# print(book)

# --------------------------------------------------------------------------------------- #

# as of Python 3.9, we can also use the 'merge' operator |

# book = book | new_items
# book |= new_items # same as 142
# print(book)

# ---------------------------------------------------------------------------------------- #

todo_1 = {'title': 'Go grocery shopping', 'completed': False, 'id': 1}
todo_2 = {'title': 'Walk the dog', 'completed': True, 'id': 2}
todo_3 = {'title': 'Practice Python', 'completed': False, 'id': 3}

# instead of multiple, individual todo item dictionaries, create a list of dicts instead
todo_list = [
    {'title': 'Go grocery shopping', 'completed': False, 'id': 1},
    {'title': 'Walk the dog', 'completed': True, 'id': 2},
    {'title': 'Practice Python', 'completed': False, 'id': 3}
]

todo_list = [
    {
        'title': 'Go grocery shopping',
        'completed': False,
        'id': 1
    },
    {
        'title': 'Walk the dog',
        'completed': True,
        'id': 2
    },
    {
        'title': 'Practice Python',
        'completed': False,
        'id': 3
    }
]


data = {
    'email': "aiefkwejf",
    'email': "aiefkwejf",
    'email': "aiefkwejf",
    'email': "aiefkwejf",
    'todos': [
        {
            'title': 'Go grocery shopping',
            'completed': False,
            'id': 1
        },
        {
            'title': 'Walk the dog',
            'completed': True,
            'id': 2
        },
        {
            'title': 'Practice Python',
            'completed': False,
            'id': 3
        }
    ]
}


# print(type(todo_list)) # <class 'list'>
# print(todo_list[0]) # {'title': 'Go grocery shopping', 'completed': False, 'id': 1}
'''

for todo in todo_list:

    # only print the incomplete todos
    if todo['completed'] == False:
        todo_output = f"""
            {todo['id']}. {todo['title']}
            Completed: {todo['completed']}"""


        print(todo_output)
        
'''


# ------------------------------------------------------------------------------- #
# nested dicts
fruits = {
    'apple': {
        'green': 2.12,
        'yellow': 3.13,
        'red': 4.14
    }
    
}

# print(fruits['apple']) # {'green': 2.12, 'yellow': 3.13, 'red': 4.14}

apple_prices = fruits['apple'] # {'green': 2.12, 'yellow': 3.13, 'red': 4.14}

# print(apple_prices['red']) # 4.14

# print(fruits['apple']['red']) # 4.14

# ---------------------------------------------------------------------------------- #

url = "https://jsonplaceholder.typicode.com/todos/7"
response = requests.get(url)

# JSON is Javascript's version of a dictionary
# convert the raw text data from JSON to Python dict
# print(response.json())

# ---------------------------------------------------- #

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

# JSON is Javascript's version of a dictionary
# convert the raw text data from JSON to Python dict
todo_list = response.json()

# print(type(todo_list)) # <class 'list'>
# print(todo_list[0]) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


for todo in todo_list:

    # only print the incomplete todos
    if todo['completed'] == False:

        # create a formatted version of the todo data
        todo_output = f"""
            {todo['id']}. {todo['title'].capitalize()}
            Completed: {todo['completed']}"""


        print(todo_output)
