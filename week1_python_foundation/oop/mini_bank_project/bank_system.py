# Mini Banking System (Improved Version)

class BankAccount:
    bank_name = "Rashid National Bank"
    account_counter = 1000

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposot amount must be positive")
            return
        
        self.__balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{amount} deposited successfully")


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        
        self.__balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        print(f"{amount} withdrawn successfully")


    def Show_balance(self):
        print(f"{self.name}'s balance is: {self.__balance}")

    def show_transactions(self):
        print(f"Transactions history for: {self.name}")
        for t in self.transactions:
            print("_", t)


# Child class

class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.interest_rate / 100 * self._BankAccount__balance
        print(f"Interest added: {interest}")

# Bank system managing multiple accounts

class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        for acc in self.accounts:
            print(acc.account_number, acc.name)


# Sysytem usage

bank = Bank()

account1 = BankAccount("Rashid", 5000)
account2 = SavingsAccount("Kofi", 10000, 5)

bank.create_account(account1)
bank.create_account(account2)

account1.deposit(2000)
account1.withdraw(1000)

account2.deposit(3000)

print("\nAll Accounts:")
bank.list_accounts()

print("\nTransactions History:")
account1.show_transactions()
