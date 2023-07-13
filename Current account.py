class CurrentAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

# Example usage

# Create a current account
account = CurrentAccount("1234567890", "John Doe")

# Deposit funds
account.deposit(1000)

# Withdraw funds
account.withdraw(500)

# Get the current balance
balance = account.get_balance()
print(f"Current balance: {balance}")
