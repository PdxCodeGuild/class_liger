

def is_valid_number(string):
    '''Return the string as a float if the string is a valid float value, otherwise False'''
    try:
        return float(string)
    except ValueError:
        return False


coin_values = {
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}

# print(coin_values.keys()) # dict_keys(['quarter', 'dime', 'nickel', 'penny'])


total = input("\nEnter a dollar amount (e.g. 1.39):\n$")

number = is_valid_number(total)
# while number == False:
# force the user to enter numbers until they enter a valid number
while not number:
    print("Please enter a valid number!")
    total = input("\nEnter a dollar amount (e.g. 1.39):\n$")

    number = is_valid_number(total)

# by the time the code reaches this point
# the user is guaranteed to have entered a valid number

# convert the dollar amount to pennies
total = int(float(total) * 100)

# # remove quarters
# quarters = total // 25
# # total = total - (quarters * 25)
# # total -= quarters * 25
# total = total % 25
# # total %= 25

# # remove quarters
# dimes = total // 10
# total = total % 10

# # remove quarters
# nickels = total // 5
# total = total % 5

output = ''
for key in coin_values:
    # retrieve the coin's value from the dict
    value = coin_values[key]

    # how many coins of the current value can be removed from total
    coin_quantity = total // value

    if coin_quantity != 0:
    # if coin_quantity:
        # add the coin's name and quantity to the string
        output += f"{key}: {coin_quantity}\n"
    
    # reduce the total to the remaining coins
    total %= value

# print(output)




