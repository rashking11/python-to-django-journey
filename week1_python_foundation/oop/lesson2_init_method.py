# Lesson 2: Using __init__ to initialize objects

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Creating objects with initial values

account1 = BankAccount("Rashid", 5000)
account2 = BankAccount("Kofi", 10000)

print(account1.name, account1.balance)
print(account2.name, account2.balance)