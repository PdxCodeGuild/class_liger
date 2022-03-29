





import random

def pick6():

    ticket_price = 2.00

    balance = 0.00

    matches = 0

    matches_list = []

    prize = 0.00

    winnings = 0

    total_winnings = ''

    winning_number = []

    for number in range(6): #for every number up to 6

        winning_number.append(random.randint(1,99)) #generate a random number and store in winning number list


    print("\n*..Pick 6 Lottery..*\n")

    print(f"\nStarting Balance: {balance}\n")

    for number in range(100000):

        balance = balance - 2.00       # balance is equal to 0 - 2 -> -2

        ticket_number = [] #ticket number has value of an empty list

        for numbers in range(6):

            ticket_number.append(random.randint(1,99))

        for index in range(6):

            if winning_number[index] == ticket_number[index]: # checks if number at index in winning number list is the same as number at that same index in ticket number list

                matches = matches + 1          # counts number of matches

    if matches == 1:                         #if number of matches = 1 then prize = 4 dollars

        prize = 4.00 

    elif matches == 2:                       # if number of matches = 2 then prize = 7 dollars

        prize = 7.00                       
        
    elif matches == 3:                        #if number of matches = 3 then prize = 100 dollars

        prize = 100.00                     

    elif matches == 4:                        #if number of matches = 1 then prize = 50000 dollars

        prize = 50000.00                    

    elif matches == 5:                        #if number of matches = 1 then prize = 1000000 dollars

        prize = 1000000.00                 

    elif matches == 6:                       # if number of matches = 1 then prize = 25000000 dollars

        prize = 25000000.00

    winnings += prize

    matches_list.append(prize)

    print(f"\nWinnings: {winnings}\n")

    balance = balance + winnings

    print(f"\nEnding Balance: {balance}\n")

pick6()