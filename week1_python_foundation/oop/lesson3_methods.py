# Lesson 3: Adding Methods to a Class

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")


    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            print(f"{amount} withdraw successfully")
    

# Create account

account1 = BankAccount("Rashid", 10000)
print("Initial balance is: ", account1.balance)

account1.deposit(5000)
print("Balance after deposit: ", account1.balance)

account1.withdraw(3000)
print("Balance after withdrawal: ", account1.balance)