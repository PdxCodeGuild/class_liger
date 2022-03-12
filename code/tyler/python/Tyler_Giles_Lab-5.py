# palindrome checker
# check if user input is == the reverse of the same user input


user_attempt = input("Enter a word: ")


user_attempt = list(user_attempt)
reversed_input = list(user_attempt)
reversed_input == reversed_input.reverse()
print(user_attempt)
print(reversed_input)


if user_attempt == reversed_input:
    print(f"\nWow. {user_attempt} is a palindrome of {reversed_input}.")
    

else:
    print(f"\n{user_attempt} is not a palindrome. ")


