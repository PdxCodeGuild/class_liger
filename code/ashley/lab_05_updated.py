import string

user_input = input('Enter a word: ')

def check_palindrome(user_input):
    input = list(user_input)
    reversed = input[::-1]
    if input == reversed:
        return f'{user_input} is a palindrome!'
    else:
        return f'{user_input} is not a palindrome!'

output = check_palindrome(user_input)

print(output)