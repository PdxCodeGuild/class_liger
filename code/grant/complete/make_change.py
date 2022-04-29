




coins = {
    'half-dollar': 50,
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}

total_amount = float(input("Please enter a dollar amount here: ")) # user input dollar amount 1.36

total = total_amount * 100    # user input converted to pennies   136          


number_of_quarters = total // coins['quarter'] # returns number of quarters in total  136/25=5

leftover_1 = total % coins['quarter'] # returns 11


number_of_dimes = leftover_1 // coins['dime'] # returns 1

leftover_2 = leftover_1 % coins['dime'] #returns 6 needs to return 1 # fixed # returns 1


number_of_nickels = leftover_2 // coins['nickel'] #returns 1

leftover_3 = leftover_2 % coins['nickel']  # 


number_of_pennies = leftover_3 // coins['penny']


quarters = int(number_of_quarters)

dimes = int(number_of_dimes)

nickels = int(number_of_nickels)

pennies = int(number_of_pennies)


print(leftover_1,
    leftover_2, 
    leftover_3,
    quarters,
    dimes,
    nickels,
    pennies  
)

print(f"You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies in U.S. coins.")