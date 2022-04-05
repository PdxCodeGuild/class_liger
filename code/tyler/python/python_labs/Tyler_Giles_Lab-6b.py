
user_credit_input = (input("Please enter your 16 digit credit card number to check validity: "))         # Exaxmple number 4556737586899855
# convert the user CC to a list of ints
user_credit_input = list(map(int, user_credit_input))

# catch inputs of less than or greater than 16 to keep programming running correctly
if len(user_credit_input) < 16:
    print("Please try again and enter a 16 digit CC number.")

elif len(user_credit_input) > 16:
    print("Please try again and enter a 16 digit CC number.")


# code block for correct amount of digits

elif len(user_credit_input) == 16:

    # slice off last digit to become the "check digit"
    check_digit = user_credit_input.pop(-1)                                                                # check_digit = 5

    user_credit_input = user_credit_input.reverse()                                                                             # number is now [5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]

    user_credit_input[::2] = [i * 2 for i in user_credit_input[::2]]                                        # number is now [10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]

    user_credit_input = [i - 9 if i > 9 else i for i in user_credit_input]                                  # number is now [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    
    # final validity check comparing modulus to check_digit
    if sum(user_credit_input) % 10 == check_digit:
        print("Valid number. Thank you for your cooperation.")
    elif sum(user_credit_input) % 10 != check_digit:
        print("Invalid number. Nice try scammer.")
