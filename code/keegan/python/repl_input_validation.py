# validate the user's input before processing their choice



def version_1():
    valid_yes = ['yes', 'y', 'yep']
    valid_no = ['no', 'n', 'nope']

    # combine all the choices into a single list
    valid_choices = valid_yes + valid_no

    while True:
        print("\nWelcome to the game!")

        # ask the user if they want to play again
        again = input("Do you want to play again? y/n: ").lower().strip().replace(' ', '')


        # VALIDATE THE USER'S INPUT
        # check to make sure the user entered a valid choice using another REPL
        # loop until the user enters a valid choice for the 'again' variable
        while again not in valid_choices:
            print("\nInvalid selection!")
            print(f"Please choose one of these: {', '.join(valid_choices)}")

            again = input("Please enter a valid selection: ").lower().strip().replace(' ', '')


        # by the time the code reaches this line,
        # the user is guaranteed to have entered a valid choice

        if again in valid_yes:
            print("Okay, let's play!")

        elif again in valid_no:
            print("Okay, Goodbye!")
            break

# version_1()


def get_valid_choice(choices: list[str]):
    '''Ask the user to enter a choice, 
    validate that it is one of the provided choices from the list and return it'''

    # ask the user if they want to play again
    again = input("Do you want to play again? y/n: ").lower().strip().replace(' ', '')


    # VALIDATE THE USER'S INPUT
    # check to make sure the user entered a valid choice using another REPL
    # loop until the user enters a valid choice for the 'again' variable
    while again not in choices:
        print("\nInvalid selection!")
        print(f"Please choose one of these: {', '.join(choices)}")

        again = input("Please enter a valid selection: ").lower().strip().replace(' ', '')

    return again


def version_2():
    # valid_yes = ['yes', 'y', 'yep']
    # valid_no = ['no', 'n', 'nope']

    # # combine all the choices into a single list
    # valid_choices = valid_yes + valid_no

    valid_choices = ['A', 'B', 'C']


    while True:
        print("\nWelcome to the game!")

        again = get_valid_choice(valid_choices)

        # by the time the code reaches this line,
        # the user is guaranteed to have entered a valid choice

        if again in valid_yes:
            print("Okay, let's play!")

        elif again in valid_no:
            print("Okay, Goodbye!")
            break

# version_2()


def is_valid_float(string: str):
    '''Check if the given string is able to be converted into a float.
    Return True if so, otherwise False'''
    try:
        float(string)
        return True

    except ValueError:
        return False


def version_3():

    number = input("Please enter a number: ")

    while not is_valid_float(number):
        number = input('Oops! Please enter a valid number: ')
    
    number = float(number)
    print(f"Thanks for entering: {number}")

# version_3()



# ------------------------------------------------------------------------------ #
