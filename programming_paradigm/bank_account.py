# Simple Bank Account Class
class BankAccount:

    # _init_ method to initialize an account_balance attribute
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    # Deposit function that adds a specified amount to account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    # Withdraw function that deducts a specified amount (handles sufficient and insufficient balances)
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    # Print the current balance         
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")