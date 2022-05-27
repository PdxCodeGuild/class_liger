'''
Datatypes:
-string (str)
    -ordered(by index) but NOT changeable
    -can retrieve with index
-integer (int)
-boolean (bool) (True or False)
-list []
    -ordered(by index) and changeable
    -to retrieve at index #print(list_name[0])
-dictionary or (dict) {}
'''

'''
Methods:
-a function that needs parentheses to be executed
-accessed using a dot after the object
-string methods:
    -.upper()
    -.title()
    -.replace('Z', 'A')
        -return new string with changes
-list methods:
    -.append(item)
        -add item to end of list
    -.insert(1, 'color')
        -add item at index and return None*
    -.extend([color_1, color_2, etc])
        -add items to end of list
    -.remove('item')
        -remove 1st occurence of item
    .pop(index)
        -remove item at index and return it
        -defaults to -1 if not provided
- random.choice(list)
    -returns random selection from list/string
'''

'''
Escape Characters:
use a backslash before the character (\)
-ex: \n = new line, \t = horizontal tab
'''

'''
Variables:
-can store any datatype
-become the datatype they store
-CAPS only if they are constant
-ex:
    counter = 1

    for color in colors:
        output = counter.(color)
        
    counter += 1
'''

'''
Functions:
-input('prompt message') - always returns a string*
-str(object) - return string of object
-int(object) - return integer (whole numbers)
-float(object) - return float (decimal numbers)
'''

'''
Arithmetic Operators:
-addition +
-subtraction -
-multiplicaion *
-exponentiation ** (x^y)
-regular division / (results in float)
-floor division // (rounds down to nearest int)
-modulus % (remainder after division)
'''

'''
Logical Operators:
-and - True if BOTH are true
-or - True if at least one is true
-not - flip a boolean
    # print(x < 0) #False
    print(not x < 0) True
'''

'''
Conditional Statements:
-if - every statement will be checked
-elif - only checked if preceding if is False
-else - only run if all other conditions are False
'''

'''
Loops:
-for loops
    -repeats until condition is met
    -for item in sequence
        -visit each item in seq
    -for x in range
        -loop certain # of times
-for/in = python operators
-item/x = any variable name to store each item
-sequence/range() = loopable object


-ex_1:
    counter = 1
    for color in colors:
            output: f string
            counter += 1 (increase the ocunter to change the number label)

-ex_2:
    powers_of_2 = []
    for exponet in range(11):
            powers_of_2.append(2 ** exponet)

-ex_3:
    numbers = []
    for x in range(10):
        random_number = random.randint(0, 100)
        numbers.append(random_number)
'''

'''
Imports
- import random - 
- import string - 
- import 
'''


# functions
def 