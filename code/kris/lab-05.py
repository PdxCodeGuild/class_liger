



palindrome = input("\nEnter a word into the palnidrome checker: ")


def checker (word):

    letter_list = list(word)
    reversed_list = list(reversed(word))

    
    if letter_list == reversed_list: 
        return True
    else:
        return False



wanted_word = checker(palindrome.lower())

if wanted_word == True:
    print(f"\n'{palindrome}' is a palindrome!")

else:
    print(f"\n'{palindrome}' is not a palindrome!")