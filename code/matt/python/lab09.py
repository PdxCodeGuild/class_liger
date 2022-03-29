from lab09_helper import verify_input, user_cards, recommendation, sum_cards


if __name__ == "__main__":

    CHOICE = "y"
    while CHOICE == "y":

        CARD_COUNT = 0
        while CARD_COUNT < 3:
            print(CARD_COUNT)
            if CARD_COUNT + 1 == 1:
                card_1 = input(">>> What's your first card? ").upper()
                print(verify_input(card_1))
            elif CARD_COUNT + 1 == 2:
                card_2 = input(">>> What's your second card? ").upper()
                print(verify_input(card_2))
            else:
                card_3 = input(">>> What's your third card? ").upper()
                print(verify_input(card_3))
            print(user_cards)
            CARD_COUNT += 1
        print(recommendation(sum_cards(user_cards)))
        CHOICE = input(">>> Would you like to play again? [y/n]: ")
        user_cards.clear()
