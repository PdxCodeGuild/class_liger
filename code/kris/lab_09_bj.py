
card_one = input("\nWhat's your first card(ex. 3 or K)?: ")
card_two = input("\nWhat's your second card(ex. 3 or K)?: ")
card_one = card_one.upper()
card_two = card_two.upper()
cards = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "A": 11
}

if card_one in cards: 
    card_one = cards[card_one]
else: 
    card_one = int(card_one)

if card_two in cards: 
    card_two = cards[card_two]
else: 
    card_two = int(card_two)
added_cards = (card_one + card_two)

if added_cards == 21: 
    print("\nBlackjack!")
elif added_cards >= 17:
    print(f"\n{added_cards}, Stay...")
elif added_cards <17:
    print(f"\n{added_cards}, Hit...")
    




    
    



    