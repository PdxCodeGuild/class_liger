# 02b lab make change

def make_change(money):
    total_pennies = money * 100
    quarters = int(total_pennies // 25)
    total_pennies = total_pennies - (quarters * 25)
    # alt total_pennies = total_pennies % 25
    dimes = int(total_pennies // 10)
    total_pennies = total_pennies - (dimes * 10)
    # alt total_pennies = total_pennies % 10
    nickels = int(total_pennies // 5)
    total_pennies = total_pennies - (nickels * 5)
    # alt total_pennies = total_pennies % 5
    remaining_pennies = int(total_pennies)
    change = {
        "quarters" : quarters , 
        "dimes" : dimes ,
        "nickels" : nickels , 
        "pennies" : remaining_pennies
    }
    return change

money = float(input("Please enter how much money you have(as a float value) so we can make change: "))

change = make_change(money)
# print(change)
for key, value in change.items():
    print(value, key)