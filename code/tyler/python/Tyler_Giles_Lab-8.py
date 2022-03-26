# buy 100k tickets then pick6 to win
# check each purchase everytime and compare winnings before buying a new ticket in the 100k loop
import random
total_balance = 0
losing_balance = 0
winning_balance = 0
winning_ticket = [] 
playing_ticket = []
tickets_bought = 0
ticket_matches = 0
match_payout_prices = { 
1 : 4,
2 : 7,
3 : 100,
4 : 50000,
5 : 1000000,
6 : 25000000}

# Generates Winning ticket
while len(winning_ticket) < 6:
    winning_ticket.append(random.randint(1, 99))


# buys a ticket 10x
while tickets_bought < 10:
    tickets_bought += 1
    # print(tickets_bought)
# generates random playing ticket
    while len(playing_ticket) < 6:
        playing_ticket.append(random.randint(1, 99))
    # print(playing_ticket)


for i in range(len(winning_ticket)):
    if playing_ticket[i] == winning_ticket[i]:
        ticket_matches += 1
        

# comparing matches and increasing match variable


print(winning_ticket)
print()
# print(playing_ticket)
print(ticket_matches)



        
# print(tickets_bought)
# print(winning_balance)
# print(playing_ticket)
# print(winning_ticket)
# print(f"${winning_balance}")