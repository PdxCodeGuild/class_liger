"""
Lab 11

version 1 & 2
rework
"""

import string


items = " "
location = 0
values_for_key_lookup = []


def lower_alphabet():
    """Returns lowsercase ascii alphabet"""
    return list(string.ascii_lowercase)


letters = lower_alphabet()

letter_dict = {letters[i]: i + 1 for i in range(0, len(letters), 1)}

rot_letter_dict = letter_dict.copy()


word = input("Enter the word to encode: ")
rotn = int(input("Enter the rotation used: "))

original_input = word

for item in word:
    if item in items:
        location = word.find(items)
        word = word.replace(item, "")
        # print(word)

word_as_list = list(word)

for key, value in letter_dict.items():
    rot_letter_dict[key] = letter_dict[key] + rotn

    if rot_letter_dict[key] > 26:
        rot_letter_dict[key] = rot_letter_dict[key] - 26
# print(rot_letter_dict)

for letter in word_as_list:
    # print(f"rotated valued: {rot_letter_dict.get(letter)}")
    values_for_key_lookup.append(rot_letter_dict.get(letter))
    cipher = []
    for number in values_for_key_lookup:
        for key, value in letter_dict.items():
            if number == value:
                # print(f"key: {key}")
                cipher.append(key)

if location > 0:
    cipher.insert(location, " ")
cipher = " ".join([str(item) for item in cipher])
print(f"\n'{original_input}' ciphered using ROT{rotn}: {cipher}")
