import random
from string import digits, ascii_uppercase as ABCs


# list comprehension formula
# 1. [expression for item in iterable (if conditional)]
# 2. [expression_1 if condition else expression_2 for item in iterable]


# generate a list of squares from 0 - 10
# numbers = []
# for x in range(11):
#     numbers.append(x**2)

numbers = [x ** 2 for x in range(11)]
# print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ----------------------------------------------------- #

colors = ['pink', 'green', 'orange', 'peach', 'yellow', 'purple']

# p_colors = []
# for color in colors:
#     if color.startswith('p'):
#         p_colors.append(color)


p_colors = [color for color in colors if color.startswith('p')]
# print(p_colors) # ['pink', 'peach', 'purple']

colors_2 = [color if color.startswith('p') else color.upper() for color in colors]
# print(colors_2) # ['pink', 'GREEN', 'ORANGE', 'peach', 'YELLOW', 'purple']

# -------------------------------------------------------- #

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(0, 100))

numbers = [random.randint(0,100) for i in range(10)]

# print(numbers) # [56, 31, 40, 13, 9, 54, 48, 82, 31, 87]



# evens = []
# for number in numbers:
#     if number % 2 == 0:
#         evens.append(number)

evens = [number for number in numbers if number % 2 == 0]
# print(evens) # [26, 34, 56, 20, 62, 92]

# ------------------------------------------------------------------- #

# print(digits) # 0123456789

# double every character in the digits string
# '012' -> '001122'

# doubled_digits = ''
# for digit in digits:
#     # 3 -> 33
#     doubled_digit = digit * 2

#     # add the doubled digit to the string
#     doubled_digits += doubled_digit

doubled_digits = ''.join([digit * 2 for digit in digits])
# print(doubled_digits) # 00112233445566778899

# --------------------------------------------------------------------------- #

# generate a string of 10 random letters and numbers
characters = doubled_digits + ABCs

# random_string = ''
# for i in range(10):
#     # generate a random character
#     random_character = random.choice(characters)

#     # add the character to the list
#     random_string += random_character

random_string = ''.join([random.choice(characters) for i in range(10)])
# print(random_string)

# list the numbers in a range objects
range_numbers = [number for number in range(10)]
# print(range_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list the colors in a reversed list of colors
reversed_colors = [color for color in reversed(colors)]
# print(reversed_colors) # ['purple', 'yellow', 'peach', 'orange', 'green', 'pink']

# filter the random characters into a list of letters and a list of digits
# input: 88WOLGA585
# output: ['8', '8', '5', '8', '5']
#         ['W', 'O', 'L', 'G' ,'A']


# number_list = []
# letter_list = []

# # print(random_string)
# # loop through all the characters
# for character in random_string:
#     # check if the character is a number or a letter
#     if character in digits:
#         # add the character to the number list
#         number_list.append(character)

#     else:
#         letter_list.append(character)

number_list = [character for character in random_string if character in digits]
letter_list = [character for character in random_string if character not in digits]

# print(''.join(number_list))
# print(''.join(letter_list))

# --------------------------------------------------------------------------- #


# check a string for doubled characters
string = 'ABCDDEFFG'

# this loop has no access to the indices of the list/string
# for letter in string:
#     print(letter)

# for index in range(len(string) - 1): # len()-1 to avoid index+1 going past the end of the list
    
#     # get the character at the current index and the one to the right of it (index+1)
#     char_1 = string[index]
#     char_2 = string[index + 1]

#     # if the two characters are the same, print the character and the indices
#     if char_1 == char_2:
#         output = f"{char_1} {index} {index + 1}"
#         print(output)

output = [(string[i], i, i+1) for i in range(len(string)-1) if string[i] == string[i + 1]]
# print(output) # [('D', 3, 4), ('F', 6, 7)]


# ----------------------------------------------------------------------------------------- #

# dict comprehension formula
# {key_expression:value_expression for key,value in iterable (if conditional)}


colors = ['pink', 'green', 'red', 'peach', 'yellow', 'teal']

# create a dictionary where the words are the keys and their lengths are the values

# color_lengths = {}
# for color in colors:
#     color_lengths[color] = len(color)

color_lengths = {color:len(color) for color in colors}

# print(color_lengths)

# filter the dictionary
color_lengths = {color:len(color) for color in colors if len(color) > 4}
# print(color_lengths) # {'green': 5, 'peach': 5, 'yellow': 6}


# ------------------------------------ #

letter_indices = [('D', 3, 4), ('F', 6, 7)]

indices_dict = {item[0]:item[1:] for item in letter_indices}
# print(indices_dict) # {'D': ([3, 4],), 'F': ([6, 7],)}

letter_indices = [('D', [3, 4]), ('F', [6, 7])]
indices_dict = dict(letter_indices)
# print(indices_dict) # {'D': [3, 4], 'F': [6, 7]}


# --------------------------------------- #


colors = ['pink', 'green', 'red', 'peach', 'yellow', 'teal']
numbers = [11, 22, 33, 44, 55, 66]

# zip(list1, list2) - combines items from list1 and list2 into a list of tuples
zipped = zip(colors, numbers)
zipped = {key:value for key,value in zipped}
# print(zipped) # {'pink': 11, 'green': 22, 'red': 33, 'peach': 44, 'yellow': 55, 'teal': 66}