

"""
Modules are just Python files.

As programs grow larger, it makes sense to break them up
into separate files (modules). Modules can then be imported
into other modules using the keyword 'import'
"""

# import <MODULE_NAME>

import random # 930 lines of code
import string # 280 lines of code

ABCs = string.ascii_uppercase
random_number = random.randint(0, 100)
random_letter = random.choice(ABCs)

# print(random_letter, random_number, ABCs)

# --------------------------------------------------------------- #

# import SPECIFIC attributes from a module

# keywords: from, import
# from <MODULE_NAME> import <ATTRIBUTE_1>, <ATTRIBUTE_2>, ... 

from random import randint, choice # imports just randint and choice instead of all 930 lines
from string import ascii_uppercase # imports 1 line instead of 280

ABCs = ascii_uppercase # shorten the variable name
random_number = randint(0, 100) # no need for 'random.' anymore
random_letter = choice(ABCs)

# print(random_letter, random_number, ABCs)

# -------------------------------------------------------------- #

# import SPECIFIC attributes from a module and change their variable name
# keywords: from, import, as

from random import randint as r_int, choice as r_choice
from string import ascii_uppercase as ABCs

random_number = r_int(0, 100)
random_letter = r_choice(ABCs)

# print(random_letter, random_number, ABCs)