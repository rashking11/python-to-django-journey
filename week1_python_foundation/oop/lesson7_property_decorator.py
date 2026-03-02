# Lesson 7: Using @property

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative")

        else: self.__balance = amount

account1 = BankAccount("Rashid", 5000)
print(account1.balance)

account1.balance = 8000
print(account1.balance)

account1.balance = -100
