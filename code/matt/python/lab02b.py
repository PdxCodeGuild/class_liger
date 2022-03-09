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

# loop through coin names to obtain key values
for key in coins.keys():

    # running total of value to subtract from dollar amount
    amount_removed = 0

    # allows loop to continue traversing dictionary when a coin prior to the end is not used
    if amount // coins[key] == 0:
        continue

    # builds # of coins & subtracts amount removed from dollar amount
    elif amount > 0 and amount // coins[key] > 0:
        coin_number = amount // coins[key]
        amount_removed = coin_number * coins[key]
        amount -= amount_removed
    # populates empty dictionary with coin name (key) and number of coins.
    # Only allows keys that do not already exist in the dictionary
    if key not in change_dict:
        change_dict.update({key: coin_number})

# results output
print("Your change is: ")
for key in change_dict:
    print(f"\t{int(change_dict[key])} {key}")
