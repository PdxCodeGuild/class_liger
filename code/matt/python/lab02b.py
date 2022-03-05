# Lab02b Make Change

#

# Amount entered - must be #
# amount converted to # of pennies
# start with largest coin
# store coin name and number - dictionary
# check if // == 0
#  - continue
# if greater than zero:
# - capture the // as the # of coin
# - multiply the // by the coin value
# - subtract this from amount
# - if amount remaining > 0 then continue to next largest coin
# - check if // is > 0
# repeat above steps until amount remaining = 0
# return text with #'s of each coin returned as change


amount = float(input("Enter a dollar amount: "))

# convert to pennies
amount *= 100

# coins & values
coins = {"quarter": 25, "dime": 10, "nickel": 5, "penny": 1}

# empty dictionary to hold coin names and number
change_dict = {}

for key in coins.keys():
    amount_removed = 0

    if amount // coins[key] == 0:
        continue

    elif amount > 0 and amount // coins[key] > 0:
        coin_number = amount // coins[key]
        amount_removed = coin_number * coins[key]
        amount -= amount_removed

    if key not in change_dict:
        change_dict.update({key: coin_number})

print("Your change is: ")
for key in change_dict:
    print(f"\t{int(change_dict[key])} {key}")
