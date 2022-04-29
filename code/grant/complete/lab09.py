





playing_cards = {
    'A' : 1 or 11,
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
    'K' : 10
}
print("\n**Blackjack Game Advice**\n")

card_1 = input("\nWhat is your 1st card?\n")

if card_1 not in playing_cards:

    raise ValueError("\nbeep boop...the program pooped\n")


card_2 = input("\nWhat is your 2nd card?\n")

if card_2 not in playing_cards:

    raise ValueError("\nnbeep boop...the program pooped\n")


card_3 = input("\nWhat is your 3rd card?\n")


if card_3 not in playing_cards:

    raise ValueError("\nbeep boop...the program pooped\n")


card_total = playing_cards[card_1] + playing_cards[card_2] + playing_cards[card_3]

if card_total < 17:

    print(f"\nYour total score is {card_total}.\n\nAdvice?: HIT!\n")

elif card_total > 17 and card_total < 21:

    print(f"\nYour total score is {card_total}.\n\nAdvice?: STAY!\n")

elif card_total == 21:

    print(f"\nYour total score is {card_total}.\n\nAdvice?: BLACKJACK!\n")

elif card_total > 21:

    print(f"\nYour total score is {card_total}.\n\nAdvice?: YOU ALREADY LOST!\n")