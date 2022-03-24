
import random

def pick_six():
    ticket = []

    for number in range(6):
        pick_nums = random.randint(1, 100)
        ticket.append(pick_nums)
    return ticket
    
def investment_return(ticket_winning, expenses):
    return ((ticket_winning - expenses) / expenses)

winn_numbers = pick_six()
ticket_winning = 0
cost_ticket = 2
num_of_tickets = 100000

"""
loop through the indices of the list, print each
use each index to print the value at that index (from both lists)
compare the values at each index and count how many match
"""

for game in range(num_of_tickets):
    matches_num = pick_six()
    lott_count = 0
    for i in range(6):
        if winn_numbers[i] == matches_num[i]:
            lott_count += 1
      

    if lott_count == 1:
        ticket_winning = ticket_winning + 4
    elif lott_count == 2:
        ticket_winning = ticket_winning + 7
    elif lott_count == 3: 
        ticket_winning = ticket_winning + 100
    elif lott_count == 4:
        ticket_winning = ticket_winning + 50000
    elif lott_count == 5:
        ticket_winning = ticket_winning + 1000000
    elif lott_count == 6:
        ticket_winning = ticket_winning + 25000000
    # print(f"You have {lott_count} matches")
   

    # ticket_winning = ticket_winning  - 2

# option 2 on pick6 lab............................



expenses = cost_ticket * num_of_tickets
earnings = investment_return(ticket_winning, expenses)



print(winn_numbers)
print(matches_num)

print(f"Your final returns on investments is: ${earnings}")