import random

"""
Anatomy of an Error Messages
----------------------------

Traceback (most recent call last):
    File "<FILENAME>.py", line number (approx)
        troublesome code (approx)
                       ^

ErrorType: specific error message
"""

# SyntaxError - a piece of code is missing or misused
# 10 / # SyntaxError: invalid syntax
# 'abc # SyntaxError: unterminated string literal (detected at line 17)
# print('hello world' # SyntaxError: '(' was never closed

# -------------------------------------------------------------------------- #

# NameError - variable or function name was used that isn't defined
# balloon # NameError: name 'balloon' is not defined
# Print() # NameError: name 'Print' is not defined. Did you mean: 'print'?

# -------------------------------------------------------------------------- #

# IndentationError - inconsistent horizontal placement

# too far right - unexpected indent
# too far left - unindent does not match any outer indentation level

# x = 4

x = 4
# if x < 10:
#     print('hello')
#   print('hello') # IndentationError: unindent does not match any outer indentation level
#      print('hello') # IndentationError: unexpected indent

# for x in range(10):
#     # blank code block
#     # IndentationError: expected an indented block after 'for' statement on line 41
#     # avoid error by using 'pass' as a placeholder
#     pass

# ----------------------------------------------------------------------------------- #

# TypeError - wrong datatype was used for an operation
# '5' + 5 # TypeError: can only concatenate str (not "int") to str
# print['hello world'] # TypeError: 'builtin_function_or_method' object is not subscriptable
# [10, 20, 30] / 10 # TypeError: unsupported operand type(s) for /: 'list' and 'int'

# ------------------------------------------------------------------------------------- #

# IndexError - index doesn't exist in an iterable (list, string, etc)
colors = ['red', 'green', 'blue']

# colors[3] # IndexError: list index out of range
# 'abc'[3] # IndexError: string index out of range

# colors[3] = 'purple' # IndexError: list assignment index out of range

# ----------------------------------------------------------------------------------- #

# AttributeError - variable, function or method doesn't belong to an object
# random.imaginary_function() # AttributeError: module 'random' has no attribute 'imaginary_function'
# 'abc'.append('d') # AttributeError: 'str' object has no attribute 'append'
# colors.capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# --------------------------------------------------------------------------------- #

# KeyError - key doesn't exist in a dictionary

example = {'a': 11, 'b': 22, 'c': 33}
# example['d'] # KeyError: 'd'

# ---------------------------------------------------------------------------------- #

# ValueError - proper datatype, but improper value was used
# int('abc') # ValueError: invalid literal for int() with base 10: 'abc'
# float('abc') # ValueError: could not convert string to float: 'abc'

# int('abc', base=2) # ValueError: invalid literal for int() with base 2: 'abc'

# ------------------------------------------------------------------------------- #

# ZeroDivisionError - division by 0
# 1 / 0 # ZeroDivisionError: division by zero

# -------------------------------------------------------------------------------- #

# Sometimes errors are trigerred in different files and will need to be tracked down

# random.choice(100)

'''
Traceback (most recent call last):
  File "C:/Users/keego/Documents/Repos/pdx_code/class_liger/code/keegan/python/error_handling.py
", line 95, in <module>
    random.choice(100)
  File "C:/Users/keego/AppData/Local/Programs/Python/Python310/lib/random.py", line 378, in choi
ce
    return seq[self._randbelow(len(seq))]
TypeError: object of type 'int' has no len()
'''

# -------------------------------------------------------------------------------- #

"""
Error Handling
Keywords: try, except, else, finally

try:
    # try to run some code
    # if an error occurs in this block
    # it can be caught and handled using an 'except' block

except ErrorType:
    # 'ErrorType' is the specific type of error we wish to catch
    # run this code block if the specified ErrorType was raised

else:
    # run this code block if no error occurred in the 'try' block

finally:
    # run this code block whether an error occurred or not

"""

# ------------------------------------------------------------------------- #

# Divide two numbers provided by the user
# Before dividing, validate that the user has entered proper numbers

"""

while True:
    try:
        x = input("Enter a number for x: ")
        y = input("Enter a number for y: ")

        # try to convert the numbers to float
        x = float(x)
        y = float(y)

        # try to divide the numbers
        quotient = x / y

    except ValueError:
        # if a ValueError was raised in the try block
        print(f"\nOne of the numbers could not be converted to float: {x}, {y}")

    # multiple except blocks for multiple types of errors
    except ZeroDivisionError:
        print("\nOops, Cannot divide by zero!")
    else:
        # if no error was raised in the try block
        print(f"\n{x} / {y} = {quotient}")
        break

    finally:
        print('\nYay, Python!')

"""


# We can raise errors ourselves and handle them.
while True:
    try:
        color = input("Enter a color: ")

        if color == 'green':
            raise ValueError("I don't like the color green!")

        print(f"I like the color {color}!")

    except ValueError as error_message:
        print(error_message)
        break
