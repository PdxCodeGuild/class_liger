'''
- string -> list & list -> string
- list slicing
- reversing lists
    - list slicing
    - reversed()
    - .reverse() - list method
- mutable vs immutable
- shallow vs deep copy
- list comprehension
'''

from string import ascii_uppercase as ABCs

# print(ABCs) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(ABCs[0]) # A

# list(sequence) - return the sequence as a list if possible
ABCs = list(ABCs)
# print(ABCs) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

string1 = 'c-a-t'
string1 = list(string1)
# print(string1) # ['c', '-', 'a', '-', 't']

# ---------------------------------------------------------------------------------------- #

'''
List Slicing

my_list[start:stop:step]

- value at the 'stop' index is not included in the final slice
- if 'start' is left blank, it will be 0 by default
- if 'stop' is left blank, it will be -1 by default
- if 'step' is blank, it will be 1 by default
'''

# indices 11-15
# print(ABCs[11:16]) # ['L', 'M', 'N', 'O', 'P']

# only a stop value
# print(ABCs[:13]) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# only a start value
# print(ABCs[13:]) # ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# move sections of the list around
# print(ABCs[13:] + ABCs[:13]) # ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# only a step value
# print(ABCs[::2]) # ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y']

# the whole list as is, start=0, stop=-1, step=1
# print(ABCs[::]) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# shorten the ABCs list 
ABCs = ABCs[:11]
# print(ABCs) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# ------------------------------------------------------------------------------------- #

# Reversing a list

# Option 1: list slicing
# print(ABCs[::-1]) # ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

# Option 2: reversed()
'''
reversed(sequence) - return a 'reversed iterator' representation of the given sequence

- the 'reversed iterator' is like a range() object and can be looped through
- it can also be converted back to a list
'''

# reverse the ABCs
# print(reversed(ABCs)) # <list_reverseiterator object at 0x0000020B498B2200>

# convert the reversed iterator of the ABCs to a list
ABCs = list(reversed(ABCs))
# print(ABCs) # ['K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

# Option 3: .reverse()
# .reverse() - reverse the list in place and return None

ABCs.reverse()
# print(ABCs) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']


# glue_string.join(list_of_strings)
# converts the list_of_strings into a single string
# by placing the 'glue_string' between each

# join the ABCs string together with a hyphen between each letter
ABCs = '-'.join(ABCs)
# print(ABCs) # A-B-C-D-E-F-G-H-I-J-K

# string.split(target) - split the string into a list of its characters at each instance of the target character
ABCs = ABCs.split('-')
# print(ABCs) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# ------------------------------------------------------------------------------------- #

# Equality vs Identity

nums1 = [2, 4, 6, 8]
nums2 = [2, 4, 6, 8]

# print(nums1 == nums2) # True - both lists have the same exact values in the same exact locations
# print(nums1 is nums2) # False - the lists are in two different places in memory


# -------------- #

nums3 = [4, 5, 6]

# doesn't make an actual copy, 
# just points to the same memory location as nums1
nums4 = nums3
# print(nums4 is nums3) # True

# changes both lists because they share one identity
nums4[0] = 9

# print(nums3, id(nums3)) # [9, 5, 6] 2524651260416
# print(nums4, id(nums4)) # [9, 5, 6] 2524651260416

# --------------- #

nums5 = [4, 5, 6]

# create a new list in memory
nums6 = nums5.copy()

nums6[0] = 9

# print(nums5, id(nums5)) # [4, 5, 6] 2378785229952
# print(nums6, id(nums6)) # [9, 5, 6] 2378785240704

# ----------------- #

string1 = 'cat'
string2 = string1
# print(string1, id(string1)) # cat 2056129794864
# print(string2, id(string2)) # cat 2056129794864

string2 = string1.replace('a','z')
# print(string1, id(string1)) # cat 2125418451760
# print(string2, id(string2)) # czt 2125418518832


