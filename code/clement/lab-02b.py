

coins = [
    'quarter', 25,
    'dime', 10,
    'nickel', 5,
    'penny', 1
]


dollar = float(input("Please enter any dollar amount:\n$"))


cent = dollar * 100


quarter = cent // 25
quarter_1 = cent % 25

dime = quarter_1 // 10
dime_1 = quarter_1 % 10


nickel = dime_1 // 5
nickel_1 = dime_1 % 5


penny = nickel_1 // 1


print(
    f"You enter: ${dollar}, {quarter} quarter, {dime} dime, {nickel} nickel, and {penny} penny")
