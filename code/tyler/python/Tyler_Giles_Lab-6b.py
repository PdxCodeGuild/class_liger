
user_credit_input = (input("Please enter your 16 digit credit card number to check validity: "))
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



    user_credit_input.reverse()

    print(check_digit)


    print(user_credit_input)

    


