import random

friends = [
    "Gaytan",
    "Ashley",
    "Tyler",
    "Clement",
]

random.shuffle(friends)

for i,friend in enumerate(friends):
    print(f"{i+1}. {friend}")