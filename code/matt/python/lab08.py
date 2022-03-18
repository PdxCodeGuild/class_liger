"""
Lab 08
Pick 6

- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000

One function you might write is `pick6()` which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be `num_matches(winning, ticket)` which returns the number of matches between the winning numbers and the ticket.

## Steps

1. Generate a list of 6 random numbers representing the winning tickets 
2. Start your balance at 0
2. Loop 100,000 times, for each loop:
3. Generate a list of 6 random numbers representing the ticket
4. Subtract 2 from your balance (you bought a ticket)
5. Find how many numbers match
6. Add to your balance the winnings from your matches
7. After the loop, print the final balance

"""

import random

TICKET_COST = 2
POTENTIAL_JACKPOTS = {"1": 4, "2": 7, "3": 100, "4": 50000, "5": 1000000, "6": 25000000}


def pick6(list_length=6):
    ticket_numbers = []
    generated_numbers = 0
    while generated_numbers < list_length:
        ticket_number = random.randrange(1, 99)
        ticket_numbers.append(ticket_number)
        generated_numbers += 1
    return ticket_numbers


def num_matches(winner: list, ticket: list) -> int:
    winners = []
    winnings = 0
    match_count = 0
    balance = 0
    balance -= TICKET_COST
    for index in range(len(winner)):
        if winner[index] == ticket[index]:
            winners.append(winner[index])
            match_count += 1
            winnings = POTENTIAL_JACKPOTS.get(str(len(winners)))
            # print(f"winner: {winners} = {winnings}")
            balance = balance + winnings

    print(f"{match_count} match(es) in round {counter +1}. Winnings & balance for the round: {winnings}, {balance}")
    return balance


if __name__ == "__main__":

    rounds = input(">>> Enter the number of rounds to play: ")
    counter = 0
    ending_balance = 0
    while counter < int(rounds):
        house_ticket = pick6(6)
        player_ticket = pick6(6)
        ending_balance += num_matches(house_ticket, player_ticket)
        counter += 1
    print(f"\nYour total ending balance is: {ending_balance}\n")
