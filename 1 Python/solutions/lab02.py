# get user input
money = round(float(input('Enter amount you want to break change: $')) * 100)

dollars = money // 100
money %= 100
quarters = money // 25
money %= 25
dimes = money // 10 
money %= 10 
nickles = money // 5
money %= 5
pennies = money

# return string/answer
print(f'Your change is {dollars} dollar(s), {quarters} quarter(s), {dimes} dime(s), {nickles} nickle(s), {pennies} penny(ies).')