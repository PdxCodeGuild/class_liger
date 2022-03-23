import string

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
total_ascii_list = lower_alphabet + upper_alphabet + numbers + special_characters
total_ascii_list.sort() # this sorts the characters into the proper order that they're listed in the ascii codes
print(len(total_ascii_list))

def rot_cipher():
    message = input('Please input a message to run through the cipher\n')
    new_message = ''
    rot_type = input('Would you like to rotate just upper/lower case letters or rotate all ascii characters in string? \nPlease type "letters" for letters or "all" for all characters.\n')
    while rot_type not in ['all', 'letters']:
        rot_type = input('That is not a valid selection. Please type "letters" to rotate letters only or "all" to rotate all characters.\n')
        
    rot_amount = int(input('How many spaces would you like to rotate each character?\n'))
    while rot_type == 'all' and rot_amount > 94:
        rot_amount = int(input('That\'s too many characters, there are only 94 characters so pick a number smaller than that please.\n'))
    while rot_type == 'letters' and rot_amount > 26:
        rot_amount = int(input('That\'s too many characters, there are only 26 characters so pick a number smaller than that please.\n'))
    
    if rot_type == 'all':
        for i in range(len(message)):
            if (total_ascii_list.index(message[i]) + rot_amount) > 94:
                difference = (total_ascii_list.index(message[i]) + rot_amount) - 94
                new_message += total_ascii_list[difference]
            else:    
                new_message += total_ascii_list[(total_ascii_list.index(message[i]) + rot_amount)]

    if rot_type == 'letters':
        for i in range(len(message)):
            if message[i] in upper_alphabet:
                if (upper_alphabet.index(message[i]) + rot_amount) > 26:
                    difference = (upper_alphabet.index(message[i]) + rot_amount) - 26
                    new_message += upper_alphabet[difference]
                else:    
                    new_message += upper_alphabet[(upper_alphabet.index(message[i]) + rot_amount)]
            elif message[i] in lower_alphabet:
                if (lower_alphabet.index(message[i]) + rot_amount) > 26:
                    difference = (lower_alphabet.index(message[i]) + rot_amount) - 26
                    new_message += lower_alphabet[difference]
                else:    
                    new_message += lower_alphabet[(lower_alphabet.index(message[i]) + rot_amount)]
            else: 
                new_message += message[i] 
    return new_message
print(rot_cipher())