card_scores = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

cards = []

while len(cards) < 3:
    card = input("Enter a card: ")
    cards.append(card)

# score = 0
# for card in cards:
#     score += card_scores[card]

# as a list comprehension
score = sum([card_scores[card] for card in cards])


if score < 17:
    advice = 'Hit!'
elif score < 21:
    advice = 'Stay!'
elif score == 21:
    advice = 'Blackjack!'
else:
    advice = 'Busted!'

print(f"Score: {score}\n{advice}")