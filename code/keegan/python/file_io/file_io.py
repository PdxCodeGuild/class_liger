import json
from multiprocessing.sharedctypes import Value
from string import punctuation


# Context manager - code block in which a connection to a resource exists
# open(filename, mode)
with open('zen_of_python.txt', 'r') as text_file: # 'r' for read mode
    # this code block is the 'context'
    # run this code with the file open
    poem = text_file.read()

# file is closed as soon as we exit the context manager's code block

# split the poem into a list of its lines
poem_lines = poem.split('\n')

# remove the first two items from the list
poem_lines = poem_lines[2::]

# combine back into a single string
poem = ' '.join(poem_lines)
# print(poem)

# initialize counter to zero for each punctuation
punctuation_counts = {punc:0 for punc in punctuation}



# loop through each character of the poem string
for character in poem:
    # if the character is a punctuation 
    if character in punctuation:
        # add the character to the count
        punctuation_counts[character] += 1



output = 'Punctuation Counts:\n'

# format all the counts into a string
for key, value in punctuation_counts.items():
    output += f"{key}: {value}\n"

with open('punctuation_counts.txt', 'w') as text_file: # 'w' for 'write' mode
    # write the output to the text file
    text_file.write(output)


# json.dumps(object) - outputs the 
punctuation_counts = json.dumps(punctuation_counts, indent=2)

with open('punctuation_counts.json', 'w') as json_file:
    json_file.write(punctuation_counts)