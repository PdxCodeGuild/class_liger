# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
# Then, figure out the point value of each card individually. 
# Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.

card_values = {                                                             # dict of card values to add
'A' : 1,
'1' : 1,
'2' : 2,
'3' : 3,
'4' : 4,
'5' : 5,
'6' : 6,
'7' : 7,
'8' : 8,
'9' : 9,
'10' : 10,
'J' : 10,
'Q' : 10,
'K' : 10,
}
user_hand = []
points = 0

user_card1 = input("What is your first card? ")                         # user inputs which cards they have
user_hand.append(user_card1.upper())                                    # add the card to the user hand list

user_card2 = input("What is your second card? ")
user_hand.append(user_card2.upper())

user_card3 = input("What is your third card? ")
user_hand.append(user_card3.upper())

for i in range(len(user_hand)):                                         # loop through the user hand list and add them up using the dict key value pairs
    points += card_values[user_hand[i]]                                 # using the user hand list as the key

if points < 17:                                                         # if statements for checking the score of your cards
    print(f"You have {str(points)} points. Best move is Hit. ")          # I would like to change this into a while loop or for loop once I am further along

elif points > 21:
    print(f"You have {str(points)} points. Sorry you busted. ")

elif points >= 17 and points < 21:
    print(f"You have {str(points)} points. Best move is Stay. ")

elif points == 21:
    print(f"You got a Blackjack! Congrats you win! ")
