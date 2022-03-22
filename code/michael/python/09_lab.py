# 09 blackjack lab
# I started working on this and kept adding features beyond the scope of the lab requirements until I realized I was building a full terminal blackjack game and decided to stop and fulfill the lab requirements so I can go back and build the full game later.
# So stand by for a fully featured blackjack game at a later time

cards_dict = {
    'A': 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def play_blackjack():
    suits = ['♠', '♥', '♦', '♣']
    winning_animation = '' # wanted to experiment with iterating through a list to create patterns
    for i in range(4):
        for r in range(len(suits)):
            # winning_animation += '\n'
            winning_animation += ' '.join(suits[r:]) + ' ' + ' '.join(suits[:r]) + '\n' 
    blackjack_image = '''
        ██████  ██       █████   ██████ ██   ██      ██  █████   ██████ ██   ██ ██
        ██   ██ ██      ██   ██ ██      ██  ██       ██ ██   ██ ██      ██  ██  ██
        ██████  ██      ███████ ██      █████        ██ ███████ ██      █████   ██
        ██   ██ ██      ██   ██ ██      ██  ██  ██   ██ ██   ██ ██      ██  ██    
        ██████  ███████ ██   ██  ██████ ██   ██  █████  ██   ██  ██████ ██   ██ ██
        '''
    print(blackjack_image)
    hand = []
    total_points = 0
    advice = ''
    card_1 = input('\nWhat is your first card: ')
    hand.append(card_1.upper())
    card_2 = input('\nWhat is your second card: ')
    hand.append(card_2.upper())
    card_3 = input('\nWhat is your third card: ')
    hand.append(card_3.upper())

    for i in range(len(hand)):
        total_points += cards_dict[hand[i]]
    if total_points > 21:
        advice = 'Already Busted!'
    elif total_points == 21:
        advice = "Blackjack" + '\n' + winning_animation
    elif total_points >= 17 and total_points <21:
        advice = 'Stay'
    elif total_points < 17:
        advice = 'Hit'

    print(str(total_points) + ' ' + advice)

play_blackjack()