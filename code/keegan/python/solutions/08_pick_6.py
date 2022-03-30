import random


def pick_6():
    '''return a list of six random integers between 1 and 99'''
    
    # define blank list
    ticket = []

    # loop 6 times
    for i in range(6):
        # generate a random integer
        random_number = random.randint(1, 99)
        # add the integer to the list
        ticket.append(random_number)

    return ticket


'''
def pick_six():
    return [random.randint(1, 99) for x in range(6)]
'''



def count_matches(winning_ticket, game_ticket):
    '''Return the number of instances where the values at a 
    particular index match between the two tickets'''
    matches = 0
    for index in range(len(winning_ticket)):
        num1 = winning_ticket[index]
        num2 = game_ticket[index]

        if num1 == num2:
            # increment the match count
            matches += 1

    return matches

'''
def count_matches_2(winner, ticket):
    return [ticket[i] for i in range(len(winner)) if winner[i] == ticket[i]]
'''


# ----------------------------------------------------------------------- #
# SETUP 
# ----------------------------------------------------------------------- #

TICKET_PRICE = 2

# Generate a list of 6 random numbers representing the winning ticket
winning_ticket = pick_6()

# Start your earnings/expenses at 0
earnings = 0
expenses = 0

payouts = {
    '0': 0,
    '1': 4,
    '2': 7,
    '3': 100,
    '4': 50e3, # 50000
    '5': 1e6, # 1000000
    '6': 25e6 # 25000000
}

# ----------------------------------------------------------------------- #
# LOOP 100k times
# ----------------------------------------------------------------------- #
for x in range(100000):
   
    # Generate a list of 6 random numbers representing the ticket
    game_ticket = pick_6()

    # Add 2 to your expenses (you bought a ticket)
    expenses += TICKET_PRICE

    # Find how many numbers match
    match_count = count_matches(winning_ticket, game_ticket)

    # ----------------------------------------------------------------------------- #
    # Add to your earnings the prize from your matches

    # with if statements
    # if match_count == 1:
    #     prize = 4
    # elif match_count == 2:
    #     prize = 7
    # elif match_count == 3:
    #     prize = 100

    # with match statement:
    # match match_count:
    #     case 1:
    #         prize = 4
    #     case 2:
    #         prize = 7
    #     case 3: 
    #         prize = 100

    # with dictionary:
    

    # pull the prize amount out of the dictionary
    prize = payouts[f"{match_count}"]

    # add the prize to the earnings
    earnings += prize

# ----------------------------------------------------------------------------- #
# After the loop, print the final balance
print(earnings)
print(expenses)

roi = (earnings - expenses)/expenses

print(roi)