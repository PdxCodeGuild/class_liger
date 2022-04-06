# Version 1
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, 
# find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

from string import ascii_lowercase
alphabet = ascii_lowercase
alphabet = list(alphabet)

user_string = input("\nWhat are you trying to encrypt Mr. Bond? ")
user_strength = int(input("How many times would you like to rotate the letters? "))


def encrypt():
    encrypted_message = []      # empty list too add message to
    for letter in user_string:
         # the letters in the string are passed into the alphabet var and then getting the index associated with it
         # then adding 
        encrypted_letter = (alphabet.index(letter) + user_strength) % 26          
        encrypted_message += alphabet[encrypted_letter]
    print(str(encrypted_message))


encrypt()