





def check_palindrome(is_palindrome):

    is_palindrome_list = list(is_palindrome)                  # word coverted to a list of letters

    is_palindrome_list.reverse()

    print(f"\nis {is_palindrome.upper()} a palindrome? ")             #prints user input

    if list(is_palindrome) == is_palindrome_list:
        print(f"\n{is_palindrome.upper()} is a Palindrome!\n")

    else:
        print(f"\n '{is_palindrome.upper()} is not a Palindrome!\n")     

def check_anagram(first_word, second_word):

    first_word.lower()

    second_word.lower()

    new_first_word = first_word.replace(' ', '')

    new_second_word = second_word.replace(' ', '')

    ana_check_1 = sorted(new_first_word)  #sorts first word list into alp order 

    ana_check_2 = sorted(new_second_word)    #sorts second word list into alp order       

    print(f"\nFirst Word: {first_word, new_first_word, ana_check_1}\n\nSecond Word: {second_word, new_second_word, ana_check_2}")             #prints user input

    if ana_check_1 == ana_check_2:

        print(f"\n{first_word.upper()} and {second_word.upper()} contain the same letters. This is an anagram!") #lets user know words are anaagrams

    else:

        print(f"\n '{first_word.upper()}' and '{second_word.upper()}' are not anagrams!")       #lets user know words are not anagrams

choice = ''

functions = {
    'palindrome_func' : check_palindrome,
    'anagram_func' : check_anagram,
    choice : ''
}

while True:

    choice = input("\nPlease choose whether you want to check if the word is an anagram or palindrome by entering 'anagram' or 'palindrome' or enter 'done' to exit: \n")

    if choice == 'palindrome':

        print('\n**PALINDROME CHECKER**\n----------------------')

        is_palindrome = input(f"\n\nPlease enter a word: ") # user inputs word

        check_palindrome(is_palindrome)

    elif choice == 'anagram':

        print('\n**ANAGRAM CHECKER**\n-------------------')

        first_word = input(f"\nPlease enter the first word: ") #user inputs first word ##### not needed

        second_word = input(f"\nPlease enter the second word: ")

        check_anagram(first_word, second_word)

    elif choice == 'done':

        print(f"\nProgram Closed\n")

        break

    else:

        print('\nInvalid Choice')