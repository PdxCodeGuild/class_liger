input = input('Enter a dollar amount: ')

user_input = float(input)

total = round(user_input * 100)

quarters = total // 25

total = total % 25

dimes = total // 10

total = total % 10

nickles = total // 5

total = total % 5

pennies = total // 1

total = total % 1

output = f"""{quarters} quarter(s), {dimes} dime(s), 
{nickles} nickle(s), and {pennies} pennies(s)"""

print(output)