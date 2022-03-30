import random
balance = 0
winning_balance = 0
winning_ticket = [] 
playing_ticket = []
tickets_bought = 0

match_payout_prices = { 
'1' : 4,
'2' : 7,
'3' : 100,
'4' : 50000,
'5' : 1000000,
'6' : 25000000}


def pick6():
    ticket = []
    while len(ticket) < 6:
        ticket.append(random.randint(1, 99))
    
    return ticket

winning_ticket = pick6()


while tickets_bought < 100000:
    pick6()
    playing_ticket = pick6()
    tickets_bought += 1
    balance += 2
    ticket_matches = 0
    for i in range(len(playing_ticket)):
        if playing_ticket[i] == winning_ticket[i]:
            ticket_matches += 1


    if ticket_matches == 1:
        winning_balance += match_payout_prices['1']

    elif ticket_matches == 2:
        winning_balance += match_payout_prices['2']

    elif ticket_matches == 3:
        winning_balance += match_payout_prices['3']

    elif ticket_matches == 4:
        winning_balance += match_payout_prices['4']

    elif ticket_matches == 5:
        winning_balance += match_payout_prices['5']

    elif ticket_matches == 6:
        winning_balance += match_payout_prices['6']
            
print(f"You spent ${balance}, and won ${winning_balance}. You have a staggering ROI of {(winning_balance - balance) / balance}! ")
        

