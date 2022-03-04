# Lab 02a Mad Libs
# version 2

"""
TODO
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.

Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

Sources:
W3 Schools for details on the Random shuffle() method
https://www.w3schools.com/python/ref_random_shuffle.asp
"""


import random


input_nouns = input("Enter five nouns separated by commas: ")
noun_list = input_nouns.split(",")
print(noun_list)

# shuffle the noun list
random.shuffle(noun_list)
# print shuffled list
# print(noun_list)

noun1 = noun_list[0]
noun2 = noun_list[1]
noun3 = noun_list[2]
noun4 = noun_list[3]
noun5 = noun_list[4]


print(
    f"""
            A {noun1.upper()} is a staple of any summer wardrobe.
            Be careful not to vacuum the {noun2.upper()} when cleaning your room.
            BBQ at my house! Everyone's invited, and don't forget it's bring your own {noun3.upper()}!
            I like my {noun4.upper()} with mustard, relish, and {noun5.upper()}.
        """
)
