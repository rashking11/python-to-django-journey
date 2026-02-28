# Lesson 6: Encapsulation

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Notice the double underscore

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account1 = BankAccount("Rashid", 5000)

print(account1.get_balance())

# Try this (will cause error)
# print(account1.__balance)