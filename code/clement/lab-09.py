

print("Welcome to Blackjack Game!")



first_card = input("Please choose your first card?\n").upper()

second_card = input("Please choose your second card?\n").upper()
third_card = input("Please choose your third card?\n").upper()

"""
create a dictionary that holds all keys and values of the playing cards

"""

playing_card = { 
    "A": 1,
    "J": 10,
    "Q": 10,
    "K": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10
}



total = playing_card[first_card] + playing_card[second_card] + playing_card[third_card]


"""
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""

if total >= 17 and total <= 21:
    print("'Stay'")
elif total < 17:
    print("'Hit'")

elif total > 21:
        print("Busted!")   
elif total == 17 and total < 21:
        print("You don't want to choose another card Stay!")
elif total == 21:
    print("Blackjack!")








   

   
















