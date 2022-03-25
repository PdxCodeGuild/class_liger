

# create an instance of our class

class ATM:   
   
    def __init__(self, balance= 0, interest_rate = 0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def str(self):
        output += "balance:"  + str(self.balance) + "\n "
        output += "interest_rate:" + str(self.interest_rate) + "\n"
        output += "deposit:" + str(self.deposit) + "\n"
        output -= "withdraw:" + str(self.balance) + "\n"
        output += "interest_rate:" + str(self.interest_rate) + "\n"
        output += "withdrawal:" + str(self.withdrawal) + "\n"
        return output

    def check_balance(self):
        self.balance
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.deposit

    def check_deposit(self, amount):
        if self.deposit < 0:
            self.deposit -= amount
            return self.balance

    def check_withdraw (self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance

    def withdrawal(self, amount):
        self.balance > amount
        return False
        

    def calc_interest(self):
        self.interest_rate *= self.balance
        return self.interest_rate

   
atm = ATM()
# balance = atm.check_balance()
# success = atm.deposit()
# success = atm.check_withdraw()
# interest = atm.calc_interest()
# print(interest)

print(f"Welcome to the ATM")

menu_options = {
'1': 'Balance',
'2': 'Deposit',
'3': 'Withdraw',
'4': 'Interest',
'5': 'Exit'
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input('\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit?\n$ '))
        success = atm.deposit(amount) # call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')
        

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdraw(amount)
        

        if not success:
            print('Insufficient funds')
            print(f'Your balance is ${atm.balance}')
        else:
            atm.withdrawal(amount)
            print(f'Withdrew ${amount}')
            

    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
        

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')