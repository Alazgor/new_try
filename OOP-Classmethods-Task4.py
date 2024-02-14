class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    @classmethod
    def from_balance(cls, starting_balance):
        new_account = cls()
        new_account.balance = starting_balance
        return new_account

    @staticmethod
    def transfer(account1, account2, amount):
        account1.withdraw(amount)
        account2.deposit(amount)

account1 = BankAccount.from_balance(100)
account2 = BankAccount()

print("Account 1 balance:", account1.balance)  # Output: 100
print("Account 2 balance:", account2.balance)  # Output: 0

BankAccount.transfer(account1, account2, 50)

print("Account 1 balance after transfer:", account1.balance)  # Output: 50
print("Account 2 balance after transfer:", account2.balance)  # Output: 50
