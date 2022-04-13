# Anonymous function with 'lambda'

# lambda param_1, param_2, etc: return value

# def add(a, b):
#     return a + b


add = lambda a, b: a + b

# print(add(5, 3))


example_dict = {
    'c': 44,
    'a': 22,
    'b': 11
}

# def sort_by_value(item):
#     return item[1]

# # key - function which returns the value by which to sort
# sorted_dict = sorted(example_dict.items(), key=sort_by_value)

sorted_dict = sorted(example_dict.items(), key=lambda item:item[1], reverse=True)

# print(sorted_dict)


animals = ['giraffe', 'tiger', 'zebra']

sorted_animals = sorted(animals, key=lambda animal:animal[-1])

print(sorted_animals)