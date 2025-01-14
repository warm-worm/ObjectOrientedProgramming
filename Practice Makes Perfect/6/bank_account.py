import random
class Bank:
    def __init__(self):
        self.balance = 0 #10**25 is the smallest 26-digit number, 10**26 -1 is the largest
        account_number = random.randint(10**25, 10**26-1) #range 2, len.... -> indices starting at 2, and every 4th index thereafter
        self.account_number = str(account_number)
        self.account_number = self.account_number[:2] + ' ' + ' '.join(self.account_number[i:i+4] for i in range(2, len(self.account_number), 4))
    def deposit(self, amount):
        amount = round(amount, 2)
        self.balance += amount
        print(f'Deposited PLN {amount} into your account.')
    def withdraw(self, amount):
        amount = round(amount, 2)
        if amount <= self.balance:    
            self.balance -= amount
            print(f'Withdrew PLN {amount} from your account.')
        else:
            print('Insufficient funds on the account.')
    def display_balance(self):
        print(f'Balance: {self.balance}')
    def display(self):
        print(f'Bank Account No: {self.account_number}')
        print(f'Balance: PLN {self.balance}')


account = Bank()
# Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
account.account_number = "12 3456 5555 9090 1111 0000 7722"
print(f'Created an account {account.account_number}')

# Display account balance
account.display_balance()

# Deposit PLN 25,30
account.deposit(25.30)
account.display()

# Withdraw PLN 31,70
account.withdraw(31.70)
account.display()

# Withdraw PLN 14
account.withdraw(14.00)
account.display()

