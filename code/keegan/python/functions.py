import random

'''
Functions

- named code blocks
- run only when called upon with parentheses after their name ()
- typically designed to perform a single task
- once defined, a function can be called as many times as needed with different data
- receive data & return data after it's been manipulated
'''

'''
# parameters are empty variables in a function's definition which await data from the function call
def function_name(parameter_1, parameter_2, ...):
    # this code block will be run
    # when the function is called

    # manipulate the parameters somehow

    # send the result back to where the function was called
    # with the keyword 'return'
    # if no return value is specified, the function will return 'None' by default
    return manipulated_parameters
    

# call the function and save the return value in a variable
returned_data = function_name(argument_1, argument_2, ...)
# data passed to functions to fill parameters are called 'arguments'
'''

# ---------------------------------------------------------------------------- #

# increment(number) - add one to the number and return the result

def increment(number):
    result = number + 1
    return result

# call the function with a value for 'number'
result = increment(9)
# print(result) # 10

result = increment(result)
# print(result) # 11

# ------------------------------------------------------------------------------- #

# arguments MUST be passed to fill parameters (unless defaults are provided)
# increment() # TypeError: increment() missing 1 required positional argument: 'number'

# ------------------------------------------------------------------------------- #

def add(a=1, b=1):
    return a + b

# if NO default values are provided for parameters
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# add(9) # TypeError: add() missing 1 required positional argument: 'b'
# print(add(9, 1)) # 10

# if default ARE provided for parameters
# print(add(10)) # 11 - (a = 10, b = default)
# print(add()) # 2 - a = default, b = default
# print(add(5, 2)) # 7 (a=5, b=2)
# print(add(b=13)) # 14 - (a=default, b=13)
# print(add(b=7, a=3)) # 10 - (a=3, b=7)

# ------------------------------------------------------------------------------ #

# 'shred' a string and return a randomized list of its characters
def shred_string(string):
    # convert the string to a list of its characters
    shreds = list(string)

    # randomize the list
    random.shuffle(shreds)

    return shreds


shredded_string = shred_string('hello world')
# print(shredded_string) # ['o', 'w', 'l', 'r', 'e', 'h', 'l', 'd', 'o', ' ', 'l']

# ------------------------------------------------------------------------------ #

def test_function():
    pass # placeholder to avoid empty code block error


# ------------------------------------------------------------------------------ #
# generate a list of 'k' integers between 'low' and 'high'

def generate_random_numbers(k, low=0, high=100):
    # create a blank list to store the numbers
    numbers = []

    # loop k times
    for num in range(k):
        # generate a random number between 'low' and 'high'
        random_number = random.randint(low, high)

        # add the random number to the list
        numbers.append(random_number)

    # return after the loop completes
    return numbers


# random_numbers = generate_random_numbers(10)
# random_numbers = generate_random_numbers(3, 10, 20)
random_numbers = generate_random_numbers(1000, -100, 100)

# print(random_numbers)

# ------------------------------------------------------------------------------------- #

# type hinting for parameters can give the user a hint as to what values to give the function
def subtract(a: int, b: int) -> int:
    '''
    DOCSTRING - provides documentation about a function, its parameters and its return value
    Return the difference of two numbers, 'a' and 'b'
    '''
    return a - b

# ----------------------------------------------------------------------------------- #

# *args - arbitrary number of arguments
# **kwargs - arbitrary number of keyword arguments a = 1
# def print_movie_ratings(*args, **kwargs):
def print_movie_ratings(*movie_titles, **ratings):
    print(ratings)
    for movie_title in movie_titles:
        # 'Fargo', kwargs['Fargo']
        print(movie_title, ratings[movie_title])

# print_movie_ratings('Sharknado', 'Frozen', 'Fargo', Sharknado=3, Frozen=2, Fargo=5)

# ----------------------------------------------------------------------------------- #

# Scope - Four 'layers' in which variables exist

# built-in, global, enclosed, local

# Built-in scope - all built-in functions, error messages, etc

x = 'global scope'

def outer_function():
    x = 'enclosed scope'

    # print(x) # enclosed scope

    def inner_function():
        x = 'local scope'

        # print(x) # local scope

        return x

    x = inner_function()

    return x

x = outer_function()

print(x) # global scope