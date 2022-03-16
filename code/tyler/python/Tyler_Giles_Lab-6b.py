
user_credit_input = (input("Please enter your credit card number to check validity: "))
# convert the user CC to a list of ints
user_credit_input = list(map(int, user_credit_input))
# slice off last digit to become the "check digit"
check_digit = user_credit_input.pop(-1)

# print(check_digit)


print(user_credit_input)