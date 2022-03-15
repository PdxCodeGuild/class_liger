
def change(amount_in_pennies): 

    quarters = amount_in_pennies // 25
    quarters_remained = amount_in_pennies % 25
    dimes = quarters_remained // 10
    dimes_remained = quarters_remained % 10
    nickels = dimes_remained // 5
    nickels_remained = dimes_remained % 5
    pennies = nickels_remained / 1

    output = ''
    if quarters >= 1: 
        output = output + f"{quarters} quarters "
    if dimes >= 1:
        output = output + f"{dimes} dimes "
    if nickels >= 1:
        output = output + f"{nickels} nickels "
    pennies = round(pennies)
    if pennies >= 1:
        output = output + f"{pennies} pennies"
    
    return output
    
original_amount = float(input("\nHow much do you want to convert?(ex. 1.36): "))

amount_in_pennies = original_amount * 100

amount_in_pennies = int(amount_in_pennies)

change_recieved = change(amount_in_pennies)
print(f"\nYour change is {change_recieved}")