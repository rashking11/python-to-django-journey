# Lesson 8: Class Methods Vs Static Methods

class BankAccount:
    bank_name = "Rashid National Bank"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Instance Method

    def deposit(self, amount):
        self.balance += amount

    # Class Method

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


    # Static Method

    @staticmethod
    def calculate_interest(amount, rate):
        return amount * rate
    

account1 = BankAccount("Rashid", 5000)

# Instance Method
account1.deposit(1000)

# Class Method
BankAccount.change_bank_name("Global Bank")

# Static Method
interest = BankAccount.calculate_interest(5000, 0.1)

print(account1.balance)
print(BankAccount.bank_name)
print("Interest:", interest)


        