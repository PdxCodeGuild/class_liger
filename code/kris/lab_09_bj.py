
card_one = input("\nWhat's your first card(ex. 3 or K)?: ")
card_two = input("\nWhat's your second card(ex. 3 or K)?: ")
card_one = card_one.upper()
card_two = card_two.upper()
faces = ["J", "Q", "K"]
ace = "A"

if card_one in faces:
    card_one = 10
elif card_one == ace:
    card_one = 11
else: 
    card_one = int(card_one)
if card_two in faces:
    card_two = 10
elif card_two == ace:
    card_two = 11
else: 
    card_two = int(card_two)
added_cards = (card_one + card_two)

if added_cards == 21: 
    print("\nBlackjack!")
elif added_cards >= 17:
    print(f"\n{added_cards}, Stay...")
elif added_cards <17:
    print(f"\n{added_cards}, Hit...")
    




    
    



    