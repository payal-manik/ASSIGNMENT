#  Implement a bank account system with deposit and withdrawal methods. 

class BankAccount:
    def __init__(self, bal=0):
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print("Deposited:", amt)

    def withdraw(self, amnt):
        if amnt <= self.bal:
            self.bal -= amnt
            print("Withdrawn:", amnt)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current balance:", self.bal)

account = BankAccount()

account.deposit(5000)
account.withdraw(1500)
account.show_balance()
