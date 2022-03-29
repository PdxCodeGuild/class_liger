
from string import ascii_lowercase as alphabet
alphabet = list(alphabet)
coded_word = ''
test_word = input("\nWhat would you like to code?: ")
times_rotated = int(input("\nHow many rotations?(ex. 13): "))
test_word = test_word.lower()  


for charcater in test_word:
    if charcater in alphabet:
        coded_letter = (alphabet.index(charcater) + times_rotated) % 26
        coded_word = coded_word + alphabet[coded_letter]

    else:
        coded_word = coded_word + charcater

print(f'''\nCoded!: 
{coded_word}''')
