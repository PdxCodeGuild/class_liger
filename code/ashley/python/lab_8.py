'''Lab 8 - Pick6'''

import random

def pick_6(unsure):
    winning_numbers = []

    for index in range(0,6):
        rand_num = random.randint(0,99)
        winning_numbers.append(rand_num)

    return winning_numbers

# what parameters do i use for this function????

# '''returns the number of matches between
# winning numbers and the ticket'''
# def num_matches(winning, ticket)




# balance = 0