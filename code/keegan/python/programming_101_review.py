# = is the assignment operator. Assigns the value on the right to the variable on the left.
# define a variable 'animal' and assign the string 'dog' to it using =

animal = 'dog'
# print(animal) # dog

# ------------------------------------------------------------------------------------- #

# a "function" is a named code block that performs a specific task
# functions are executed by placing parentheses () after their name
# data can be passed into the function by placing it within the parentheses
# functions will always return a value as well

# type(object) - return the datatype of the object
animal_datatype = type(animal)
# print(animal_datatype) # <class 'str'>

# print('The datatype of the animal variable is ' + str(type(animal)))


# string (str) - sequence of textual characters surrounded by quotes
# --------------------------------------------------------------------------------------- #

# change the value within the variable 'animal' to 'cat'
animal = 'cat'
# print(animal) # cat


# --------------------------------------------------------------------------------------- #

# concatenation - adding strings together to form a single string

# add the string 'fish' to the value within the variable 'animal'
# redefined 'animal' with the result
animal = animal + 'fish'
# print(animal) # catfish

# --------------------------------------------------------------------------------------- #

# a 'method' is a function that manipulates only the object to which it belongs
# an object's methods are accessed using a dot after the object's name

# .upper() - return an uppercase version of the string

# print(animal).upper() # NoneType object has no attribute upper (only strings have .upper())
# print(animal.upper()) # CATFISH (.upper() doesn't change the value in the variable)
# print(animal) # catfish

# .replace(old, new) - return a copy of the string with the old replaced with the new within it
# print(animal.replace('c', 'b')) # batfish
# print('abcabc'.replace('a', 'z')) # zbczbc

# the third argument is how many instance of the old we want to replace
# print('abcabc'.replace('a', 'z', 1)) # abczbc

# methods can be chained. Each one operates on the return value of the previous
# print(animal.replace('c', 'b').upper()) # BATFISH

# print('a-b-c'.split('-')) # ['a', 'b', 'c']
# print('a-b-c'.split('-').upper()) # AttributeError: 'list' object has no attribute 'upper'

# ---------------------------------------------------------------------------------------------- #

"""
Escape Characters

- Denoted with a backslash \ before the character 
- "Escape" the normal rules of strings to allow the characters to behave differently than normal
"""

# print("hello "world"") # Error! Quotes cancel each other

# Solution 1 - printing quotes with mismatched sets:
# print('hello "world"') # hello "world"
# print(f"{'hello'.replace('h', 'j')}") # jello

# Solution 2 - printing quotes with escape characters
# print("hello \"world\"") # hello "world"

# formatting string with escape characters
# print("A\nB\nC") # \n - new line character
# print("A\tB\tC") # \t - horizontal tab character

# ------------------------------------------------------------------------------------------- #

'''
Python Variable Names

- must start with a letter or underscore
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words, separated with underscores

# ThisIsPascalOrTitleCase - used for defining classes in Python
# ALLCAPS - generally used for constant variables

# for Python styling conventions check out PEP8 (Python Style Guide)

# ----------------------------------------------------------------------------------------- #

# f-strings
# 'f' stands for 'formatted'. f-strings allow Python expressions to be formatted into strings

# note: concatenation only works with strings
# other datatypes will need to be "typecast" using str() before concatenation

number = 99.5
output = 'The number is ' + str(number) + '!'
# print(output) # The number is 99.5!

# f-strings don't care about datatype
output = f"The number is {number}!"
# print(output) # The number is 99.5!

# ----------------------------------------------------------------------------------------- #
'''
user_string = input(prompt_message)

Print the prompt message and wait for the user to hit enter.
Once the user hits enter, anything they typed in the terminal will be returned.
Return value can be saved in a variable such as 'user_string'
'''

# name = input('Enter your name: ')
# print(f"Hello, {name}!") # Hello, Keegan!

# ------------------------------------------------------------------------------------------ #
'''
# input() always returns a string

# typecast to a number
# int(object) - return the object as an integer, if possible
# float(object) - return the object as a float, if possible


number = input('Enter a number: ')
print(number, type(number)) # 9 <class 'str'>
print(number * 10) # 9999999999

# convert the number string to float
number = float(number)
print(number, type(number)) # 9.0 <class 'float'>
print(number * 10) # 90.0
'''

# ----------------------------------------------------------------------------------------- #

# integer (int) - whole numbers
# float (float) - decimal numbers

# arithmetic operators
x = 5
y = 3

# print(x + y) # addition +
# print(x - y) # subtraction -

# print(x * y) # multiplication *
# print(x ** y) # exponentiation ** (x^y)

# print(x / y) # 'regular' division / (results in a float)
# print(x // y) # 'floor' division // (rounds down to the nearest integer)

# print(x % y) # modulus % (remainder after division)

# ----------------------------------------------------------------------------------- #

# ReAssignment Operators

x = 4

# print(x + 3) # 7 - uses x but doesn't change x
# print(x) # 4

x = x + 3
# print(x)

# ReAssignment operators exist for each arithmetic operators
# -=, *=, **=, /=, //=, %=

# ----------------------------------------------------------------------------------------- #

'''
booleans, comparisons, logical statements, conditionals
'''

# datatype - boolean
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# booleans in Python are Capitalized
# a = false # NameError: name 'false' is not defined. Did you mean: 'False'?

# -------------------------------------------------------------------------------------- #

# typecast to boolean
# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# if an object has value, it will convert to True
# if an object has no value, it will convert to False

# print(bool([])) # False
# print(bool(['a'])) # True

'''
# Falsey values
''    # blank string has no value
[]    # blank list has no value
0     # number 0 has no value
None  # None has no value
etc...
'''

# -------------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean

# All comparisons need two sides

x = 5
y = 5

# print(x == y) # == check equality - True
# print(x != y) # != check inequality - False

# print(x < y)  # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y) # > 'strictly' greater than - False
# print(x >= y ) # >= greater than or equal to - True

# ---------------------------------------------------------------------------------------- #

# Logical Operators - combine comparisons and result in a single boolean
# and, or, not

# logical statements need two comparisons

x = 5
y = 5

# and - True only if BOTH comparisons are True
# print(x == 5 and y == 5) # True - both comparisons are True
# print(x == 5 and y == 2) # False - left comparison (x == 2) is False

# or - True if at least ONE comparison is True
# print(x == 5 or y == 2) # True - left comparison (x == 5) is True
# print(x == 10 or y == 2) # False - both comparisons are False

# not - flip a boolean
# print(not True) # False
# print(not False) # True

# 'not' is often used with the keyword 'in' to check if an item is in a sequence
# print(33 in [11, 22, 33]) # True
# print(44 not in [11, 22, 33]) # True

# ---------------------------------------------------------------------------------------- #

'''
Conditional Statements
----------------------
Run different code blocks based on the outcome of comparisons
Keywords: if, elif, else

Code Block:
A section of code that executes together.
In Python, code blocks are defined using horizontal indentation

---------------------------------------------------------------------------------------

Conditional Rules:
------------------

- must start with if
- all ifs will be checked
- elif are only checked if the preceding if and other elifs were False
- else is triggered if all other conditions were False
- if/elif will only be checked until a True condition is found

---------------------------------------------------------------------------------------

Conditional Statements Will Always Have:
------------------------------------------
- 1 if
- 0 -> infinity elifs
- 0 or 1 else

'''

x = 5

if x > 5:
    print(f"{x} is greater than 5")

elif x < 5:
    print(f"{x} is less than 5.")

else:
    print('x is 5')

# ------------------------------------------------------------------------------------------- #

'''
Unit 4 - lists / for loops
------

Datatype: list

Lists are 'ordered' and 'changeable' sequences of items.
Lists are created using square brackets []
List items are separated with commas ,
'''

# define a list of colors

# organized vertically

# ------------------------------------------------------------------------------------------- #

# list items can be retrieved using their positions in the list
# an item's position in the list is called its 'index'

# place the index of the item in square brackets
# after the list's variable name to retrieve the item
# list indices always start at 0


# can't use non-existent indices

# In Python, negative indices are allowed
# -1 will always be the last index

# # can't use non-existent indices

# ------------------------------------------------------------------------------------ #

# strings are ordered sequences as well

# strings are NOT 'changeable'

# lists ARE changable

# ------------------------------------------------------------------------------------- #

# cannot add values this way

# items can be added using list methods

# .append(item) - add a single item to the end of the list

# .insert(index, item) - add the item at the index

# .extend(sequence) - add the items from the sequence to the end of the list

# -------------------------------------------------------------------------------------- #

# items can be removed with list methods as well

# .remove(item) - remove the first occurrence of the item from the list

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided

# ------------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order (returns None)

# .sort() returns None

# ---------------------------------------------------------------------------------------------- #


# loop - a code block that repeats until a certain condition is met

# for item in sequence - loop through each item in the sequence

# for/in - Python operators
# item - arbitrary variable name to store each item as the loop visits it
# sequence - string, list or other 'iterable' (loopable) object

# ---------------------------------------------------------------------------------------------- # 
# for x in range() - loop a certiain number of times

# range(stop) - return a range of numbers from 0 to stop-1

# range(start, stop, step)

# -------------------------------------------------------------------------------------- #

# while loop

'''
while some_condition == True:
    # loop this
    # code block
'''

# -------------------------------------------------------------------------------------- #

# loop controls
# continue, break, else
