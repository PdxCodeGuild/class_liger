





cypher = {
    " " : " ",
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m"
}


print("\n              **ROT CIPHER**\n")


message_string = []

coded_message = ''

loop_until = True

quit = 'quit'

message = ''

    
while loop_until:

    message = input("\nPlease enter the message you would like to encrypt: (enter 'quit' to close.)\n\n")    

    coded_message = ''

    message_string = []

    if message == quit:

        loop_until = False 
            
        print("\nProgram Terminated\n")

        break

    for character in message:

        message_string.append(character)

    for letter in message_string:    

        if letter not in cypher:

            pass
            
        else:        

            coded_message += cypher[letter]

    print(f"\nCoded Message: {coded_message}\n")
