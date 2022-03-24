# ATM LAB

class ATM:
    def __init__(self, bal, interest):
        self.bal = bal
        self.interest = interest
        self.transactions = []

    def check_balance(self):
        balance = self.bal
        return balance

    def deposit(self, amount):
        self.bal += amount
        self.transactions.append(f'user deposited ${amount}')
    
    def check_withdrawal(self, amount):
        if amount <= self.bal:
            success = True
        else:
            success = False
        return success

    def withdraw(self, amount):
        self.bal -= amount
        self.transactions.append(f'user withdrew ${amount}')
    
    def calc_interest(self):
        amount = self.interest * self.bal * .01
        return amount

    def print_transactions(self):
        trans = self.transactions
        return trans
    
#################################################
# The portion copied from the lab

atm = ATM(100, 1) # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Transactions',
    '6': 'Exit'
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
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount) # call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    
    elif command == 'Transactions':
        trans = atm.print_transactions()
        print("The following is a list of your transactions:\n")
        for i in range(len(trans)):
            print(trans[i])
        print('That concludes your list of transactions.')

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')