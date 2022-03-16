import string
from unittest import result

user_input = input('Enter a word: ')

letters = []

def shred_string(string):
    letters = list(string)
    return letters

result_1 = shred_string(user_input)
print(result_1)

def check_palindrome(letters):
    result = list(reversed(letters))
    return result

result_2 = check_palindrome(user_input)
print(result_2)

if result_1 == result_2:
    print(f'{user_input} is a palindrome!')
else:
    print(f'{user_input} ia not a palindrome...')