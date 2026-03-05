# Mini Banking System (OOP Practice)

class BankAccount:
    bank_name = "Rashid National Bank"

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        
        self.__balance += amount
        print(f"{amount} deposited successfully")


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")


    def show_balance(self):
        print(f"{self.name}'s balance is: {self.__balance}")


# Child class using inheritance

class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self,self.interest_rate
        print(f"Interest rate for {self.name} is {interest}%")

    
# Creating objects

account1 = BankAccount("Rashid", 5000)
account2 = SavingsAccount("Kofi", 10000, 5)

# Using methods

account1.deposit(2000)
account1.withdraw(1000)
account1.show_balance()

print("------------------")

account2.deposit(3000)
account2.add_interest()
account2.show_balance()

