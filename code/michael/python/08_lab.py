# Pick 6

import random

balance = 0
winning_numbers = []
your_numbers = []
matches = 0
earnings = 0
expenses = 0 
roi = 0


def pick6():
    numbers = []
    for i in range(6):
        new_num = random.randint(1, 99)
        numbers.append(new_num)
    return numbers

def ret_on_inv(earnings, expenses):
    roi = (earnings - expenses) / expenses
    return roi

# print(pick6())

winning_numbers = pick6()

for i in range(100000):
    your_numbers = pick6()
    balance -= 2
    expenses += 2
    for i in range(6):
        if your_numbers[i] == winning_numbers[i]:
            matches += 1
    if matches == 1:
        balance += 4
        earnings += 4
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 6:
        balance += 25000000
        earnings += 25000000
    matches = 0
    
print(winning_numbers)
print(your_numbers)
print(f'Congratulations! Your final balance is ${balance}!')
print(f'\nWith an earnings of ${earnings} and an investment of ${expenses}, your ROI is {ret_on_inv(earnings, expenses)}! Congratulations on such a wise investment!')
