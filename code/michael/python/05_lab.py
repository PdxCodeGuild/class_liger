# palindrome checker

def check_pal(word):
    # print(word)
    word_list = word.lower()
    word_list = list(word_list)
    # print(word_list)
    reversed_word_list = word_list.copy()
    reversed_word_list.reverse()
    if reversed_word_list == word_list:
        return True
    else:
        return False

# print(check_pal('racecar'))
# print(check_pal('cockroach'))

word = input("enter a word to check: ")
if check_pal(word) == True:
    is_pal = 'is a palindrome'
else:
    is_pal = 'is not a palindrome'
print(f"\n{word} {is_pal}")