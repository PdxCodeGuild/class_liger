
original_amount = float(input("\nHow much do you want to convert?(ex. 1.36): "))
amount_in_pennies = original_amount * 100
def change(amount_in_pennies): 

    quarters = amount_in_pennies // 25
    quarters_remained = amount_in_pennies % 25
    dimes = quarters_remained // 10
    dimes_remained = quarters_remained % 10
    nickels = dimes_remained // 5
    nickels_remained = dimes_remained % 5
    pennies = nickels_remained / 1

    if quarters >= 1: 
        quarters_total = (str(quarters) + " quarters")
    else: 
        quarters_total = "0 quarters"
    if dimes >= 1:
        dimes_total = (str(dimes) + " dimes")
    else:
        dimes_total = "0 dimes"
    if nickels >= 1:
        nickels_total = (str(nickels) + " nickels")
    else:
        nickels_total = "0 nickels"
    pennies = round(pennies)
    if pennies >= 1:
        pennies_total = (str(pennies) + " pennies")
    else:
        pennies_total = "0 pennies"
    
    total_change_list = [quarters_total, dimes_total, nickels_total, pennies_total]

    if quarters == 0:
        total_change_list.remove(quarters_total)
    if dimes == 0:
        total_change_list.remove(dimes_total)
    if nickels == 0:
        total_change_list.remove(nickels_total)
    if pennies == 0:
        total_change_list.remove(pennies_total)
    


    return  total_change_list


change_recieved = change(amount_in_pennies)
print(change_recieved)