user_amount = float(input("Please enter a dollar amount so we can make change for it: "))        # user inputting their desired dollar amount
total_cents = float(user_amount * 100)        # convert the input to a float to represent pennies

quarters = total_cents // 25                        #create variable for quarters using floor division
total_cents = total_cents - quarters * 25
dimes = total_cents // 10                       #create variable for dimes using floor division
total_cents = total_cents - dimes * 10
nickels = total_cents // 5                      #create variable for nickels using floor division
total_cents = total_cents - nickels * 5
pennies = total_cents // 1                      #create variable for pennies using floor division
total_cents = total_cents - pennies

quarters = int(quarters)                # convert the variables to integers to remove the decimal

dimes = int(dimes)              # convert the variables to integers to remove the decimal

nickels = int(nickels)              # convert the variables to integers to remove the decimal

pennies = int(pennies)              # convert the variables to integers to remove the decimal

output = f"You entered {user_amount}. \n The change for the amount you entered is \n {quarters} quarters, \n {dimes} dimes, \n {nickels} nickels, \n and {pennies} pennies."
# create the output variable with an "f string" and line breaks for readability

print(output)