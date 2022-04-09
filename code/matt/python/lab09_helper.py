"""Dictionary of card values"""
card_values_dict = {
    "A": 1,
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
    "K": 10,
}

INPUT_STRING = "A2345678910JQK"


user_cards = []

CARD_COUNT = 0


def verify_input(card: str):
    """Verifies user only inputs card values"""

    while card not in INPUT_STRING:
        print("Card valuse are: A,2,3,4,5,6,7,8,9,10,J,Q,K\n")
        if CARD_COUNT + 1 == 1:
            card = input(f">>> What's first your card? ").upper()
        elif CARD_COUNT + 1 == 2:
            card = input(">>> What's your second card? ").upper()
        elif CARD_COUNT + 1 == 3:
            card = input(">>> What's your third card? ").upper()
    user_cards.append(card)
    return user_cards


def sum_total(nums: list):
    """summing function called in sum_cards to sum card values"""
    total = 0
    for num in nums:
        total += num
    return total


def sum_cards(cards: list[str]) -> int:
    """Totals value of cards in hand"""
    hand = []
    for card in cards:
        hand.append(card_values_dict[card])
    hand_total = sum_total(hand)
    return hand_total


def recommendation(card_total: int) -> str:
    """Generates recommendation based on hand value genreated in sum_cards"""
    if card_total > 21:
        result = f"{card_total} - Already Busted"
    elif card_total == 21:
        result = f"{card_total} - Blackjack"
    elif card_total >= 17 and card_total < 21:
        result = f"{card_total} - Stay"
    else:
        result = f"{card_total} - Less than 17 - Hit"

    return result
