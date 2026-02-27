# Lesson 5: Class variable vs instance variable

class BankAccount:
    bank_name = "Rashid national Bank"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


account1 = BankAccount("Rashid", 5000)
account2 = BankAccount("Kofi", 7000)

print(account1.bank_name)
print(account2.bank_name)