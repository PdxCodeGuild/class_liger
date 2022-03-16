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
    check_digit = user_credit_input.pop(-1)
    print(check_digit)

    user_credit_input.reverse()
    print(user_credit_input)

    user_credit_input[::2] = [i * 2 for i in user_credit_input[::2]]
    print(user_credit_input)

    user_credit_input = [i - 9 if i > 9 else i for i in user_credit_input]
    print(user_credit_input)

    print(sum(user_credit_input))
    if sum(user_credit_input) % 10 == check_digit:
        print("Valid")


