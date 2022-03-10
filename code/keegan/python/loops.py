import random
from string import digits, ascii_uppercase as ABCs

# generate a list of squares from 0 - 10
numbers = []
for x in range(11):
    numbers.append(x**2)

# ----------------------------------------------------- #

colors = ['pink', 'green', 'orange', 'peach', 'yellow', 'purple']

p_colors = []

for color in colors:
    if color.startswith('p'):
        p_colors.append(color)

# print(p_colors) # ['pink', 'peach', 'purple']

# -------------------------------------------------------- #

numbers = []
for i in range(10):
    numbers.append(random.randint(0, 100))

# print(numbers) # [56, 31, 40, 13, 9, 54, 48, 82, 31, 87]

evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

# print(evens) # [26, 34, 56, 20, 62, 92]

# ------------------------------------------------------------------- #

# print(digits) # 0123456789

# double every character in the digits string
# '012' -> '001122'

doubled_digits = ''
for digit in digits:
    # 3 -> 33
    doubled_digit = digit * 2

    # add the doubled digit to the string
    doubled_digits += doubled_digit

# print(doubled_digits) # 00112233445566778899

# --------------------------------------------------------------------------- #

# generate a string of 10 random letters and numbers
characters = doubled_digits + ABCs

random_string = ''
for i in range(10):
    # generate a random character
    random_character = random.choice(characters)

    # add the character to the list
    random_string += random_character

# print(random_string)


# filter the random characters into a list of letters and a list of digits
# input: 88WOLGA585
# output: ['8', '8', '5', '8', '5']
#         ['W', 'O', 'L', 'G' ,'A']


number_list = []
letter_list = []

# print(random_string)
# loop through all the characters
for character in random_string:
    # check if the character is a number or a letter
    if character in digits:
        # add the character to the number list
        number_list.append(character)

    else:
        letter_list.append(character)

# print(''.join(number_list))
# print(''.join(letter_list))

# --------------------------------------------------------------------------- #


# check a string for doubled characters
string = 'ABCDDEFFG'

# this loop has no access to the indices of the list/string
# for letter in string:
#     print(letter)

for index in range(len(string) - 1): # len()-1 to avoid index+1 going past the end of the list
    
    # get the character at the current index and the one to the right of it (index+1)
    char_1 = string[index]
    char_2 = string[index + 1]

    # if the two characters are the same, print the character and the indices
    if char_1 == char_2:
        output = f"{char_1} {index} {index + 1}"
        # print(output)


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #





'''
Watch out for shortening lists while looping.

AABCDE
i              i = 0, first A removed

ABCDE
 i             i=1, second A is missed because it is now at index 0


character_list = list(random_string)
# print(character_list)

for i in range(len(character_list)):
    character = character_list[i]
    
    # check if the character is a digit
    if character.isdigit():
        character_list.pop(i)
'''




'''
Fix with a while loop:

AABCDE
i              i = 0, first A removed, decrease i by 1

ABCDE
i              i = 0, second A is removed because i is 0 again
'''

character_list = list(random_string)


index = 0
while index < len(character_list):
    character = character_list[index]
    
    # if the character is a number
    if character.isdigit():
        # remove the item at the current index
        character_list.pop(index)

        # decrease the index to accomodate the loss of list length
        index -= 1

    index += 1

# print(character_list)

# --------------------------------------------------------------------------- #


tic_tac_toe = [
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],
]

# print(tic_tac_toe[0][2])


grid = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y', 'Z'],
]

vowels = ['A', 'E', 'I', 'O', 'U']

for row_index in range(len(grid)):
    # use the row index to get the row list from the grid
    row = grid[row_index]

    # loop through the indices of the row list
    for col_index in range(len(row)):
        # use the col index to get the current letter from the row
        letter = row[col_index]

        if letter in vowels:
            print(f"{letter} - ({row_index}, {col_index})")