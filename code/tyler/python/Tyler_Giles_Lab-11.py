# Version 1
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, 
# find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

from string import ascii_lowercase
alphabet = ascii_lowercase
alphabet = list(alphabet)
# print(alphabet)

# user_string = input("\nWhat are you trying to encrypt Mr. Bond? ")
# user_strength = int(input("How many times would you like to rotate the letters? "))
user_string = "abc"
user_string = list(user_string)
# user_string = list(user_string)
user_strength = 13
def encrypt():
    encrypted_message = []
    for index in range(len(user_string)):
        print(user_string.index)

    # for i in range(len(user_string)):
    #     encrypted_char = user_string[i] + user_strength
    # encrypted_message.append(encrypted_char)
    # print(encrypted_message)

encrypt()