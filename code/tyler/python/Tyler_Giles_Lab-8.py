import random

def pick6():
    balance = 0
    winning_ticket = []  
    tickets_bought = 0
    # print("\nGenerating winning numbers and tickets... ")
    while tickets_bought < 100000:                              
        if len(winning_ticket) < 6:
            winning_ticket.append(random.randint(1, 99))
        tickets_bought += 1
        balance -= 2
        
    print(winning_ticket)


pick6()