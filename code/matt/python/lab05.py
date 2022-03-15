# Lab 05 Palindrome Checker

"""
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.
"""

# user enter word - ? - spaces
# create palindrome function
# user input function argument
# reverse the word
# check if the word =s its reverse
# - if equal says its a palindrome
# - if not equal say its not a palindrome

user_word = input(">>> enter a word: ")


def check_palindrome(word: str) -> str:
    if word == word[::-1]:
        result = f">>> '{word}' is a palindrome"
    else:
        result = f">>> '{word}' is not a palindrome"
    return result


print(check_palindrome(user_word))
