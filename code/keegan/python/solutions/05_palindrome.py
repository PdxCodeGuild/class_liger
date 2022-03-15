
def check_palindrome_1(word):

    letter_list = list(word)

    word_reversed = []
    # while letter_list != []:
    # while letter_list:
    while len(letter_list) > 0:
        # remove the last letter
        letter = letter_list.pop()

        # add the letter to the reversed list
        word_reversed.append(letter)

    # join back into a string
    word_reversed = ''.join(word_reversed)

    if word == word_reversed:
        return True
    else: 
        return False

def check_palindrome_2(word):

    reversed_word = ''

    # loop from the last index to the first index, counting by -1
    for index in range(len(word)-1, -1, -1):
        letter = word[index]

        reversed_word += letter

    # return the boolean resulting from the expression
    return word == reversed_word


def check_palindrome_3(word):
    reversed_word = list(word)

    # list method to reverse a list
    reversed_word.reverse()

    # join into a string
    reversed_word = ''.join(reversed_word)

    return word == reversed_word


def check_palindrome_4(word):
    word = list(word)
    reversed_word = list(reversed(word))
    return reversed_word == word

    # in one line:
    # return list(word) == list(reversed(word))

def check_palindrome_5(word):
    return word == word[::-1]



word = input("Enter a word to check if it is a palindrome:\n> ")
# replace empty spaces with blank strings
word = word.replace(' ', '')

# print(check_palindrome_1(word))
# print(check_palindrome_2(word))
# print(check_palindrome_3(word))
# print(check_palindrome_4(word))
print(check_palindrome_5(word))