"""
Lab 11

version 1 & 2
"""

import string


items = " "
location = 0


def lower_alphabet():
    """Returns lowsercase ascii alphabet"""
    return list(string.ascii_lowercase)


def get_value(letter: str, rotation: int = 13) -> int:
    """Returns value associated with letter key value from letter_dict. Corrects for values greater than 25"""
    if rotation < (max_value / 2) - 1:
        letter_value = letter_dict.get(letter)
        # print(rotation)
        # print(f"{letter}, {letter_value}")
        if letter_value > rotation:
            letter_value = letter_value - rotation
            return letter_value
        else:
            return letter_value + rotation
    else:
        letter_value = letter_dict.get(letter)

        if letter_value + rotation < max_value:
            letter_value = letter_value + rotation
            # print("get value: ", letter_value)
            return letter_value
        else:
            # print(f"{letter}, {letter_value}")
            return letter_value + rotation - max_value


def get_key(val: int) -> str:
    """Returns letter (key) based on the adjustments applied in get_value"""
    for key, value in letter_dict.items():
        if val == value:
            return key
    return f"{val} no key"


def ciphered_word(user_input: list[str]) -> str:
    """Prints output ciphered by rotation input by user"""
    cipher = []
    for letter in word_as_list:
        value = get_value(letter, rotn)
        cipher.append(get_key(value))
    if location > 0:
        cipher.insert(location, " ")
    cipher = " ".join([str(item) for item in cipher])
    print(f"\n'{original_input}' ciphered using ROT{rotn}: {cipher}")


if __name__ == "__main__":

    letter_dict = {lower_alphabet()[i]: i for i in range(0, len(lower_alphabet()), 1)}
    max_value = len(lower_alphabet())

    word = input("Enter the word to encode: ")
    rotn = int(input("Enter the rotation used: "))
    original_input = word

    for item in word:

        if item in items:

            location = word.find(items)

            word = word.replace(item, "")

    word_as_list = list(word)

    ciphered_word(word_as_list)
