# ============================================
# MINI BANKING SYSTEM (PROFESSIONAL VERSION)
# ============================================

class BankAccount:
    # Class variables (shared across all instances)
    bank_name = "Rashid National Bank"
    account_counter = 1000

    def __init__(self, name, balance):
        self.name = name

        # 🔒 Private attribute (encapsulation)
        # This prevents direct modification like: acc.__balance = -1000
        self.__balance = balance

        # Auto-generate account number
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

        # Store transaction history
        self.transactions = []
        self.load_transaction()

    # ============================================
    # 🟢 GETTER (READ VALUE SAFELY)
    # ============================================
    @property
    def balance(self):
        """
        This method allows us to access __balance like a variable:
            acc.balance

        Internally, Python calls this method automatically.
        This gives us CONTROL over how balance is accessed.
        """
        return self.__balance

    # ============================================
    # 🔵 SETTER (MODIFY VALUE SAFELY)
    # ============================================
    @balance.setter
    def balance(self, amount):
        """
        This method is triggered when we assign:
            acc.balance = value

        It allows us to:
        - Validate input
        - Prevent invalid states (e.g., negative balance)
        - Control how data is modified
        """
        if not isinstance(amount, (int, float)):
            print("Amount must be a number!")
            return

        if amount < 0:
            print("Balance cannot be negative!")
            return

        # Only update if validation passes
        self.__balance = amount


    # ============================================
    # SAVE FUNCTION
    # ============================================

    def save_transaction(self, transaction):
        
        # Save transactions to a file specific to the account
        filename = f"{self.account_number}.txt"
        with open(filename, "a") as file:
            file.write(transaction + "\n")

    

    # ============================================
    # LOAD TRANSACTIONS FUNCTION
    # ============================================


    def load_transaction(self):

        # Loads existing transactions from file when account is created.
        filename = f"{self.account_number}.txt"

        try:
            with open(filename, "r") as file:
                self.transactions = [line.strip() for line in file]
        except FileNotFoundError:
            self.transactions = []




    # ============================================
    # 💰 DEPOSIT METHOD
    # ============================================
    def deposit(self, amount):
        """
        Business logic method.
        NOTE:
        - No input() here (separation of concerns)
        - This method assumes it receives clean data
        """
        if not isinstance(amount, (int, float)):
            print("Invalid input. Enter numbers only.")
            return

        if amount <= 0:
            print("Deposit amount must be greater than 0")
            return

        # 🔥 This triggers:
        # 1. Getter → self.balance
        # 2. Addition
        # 3. Setter → self.balance = new value
        self.balance += amount

        transaction = f"Deposited {amount}"
        self.transactions.append(f"Deposited {amount}")
        # Save Transaction now
        self.save_transaction(transaction)
        print(f"{amount} deposited successfully")

    # ============================================
    # 💸 WITHDRAW METHOD
    # ============================================
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Invalid input. Enter numbers only.")
            return

        if amount <= 0:
            print("Invalid amount")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        # Again uses getter + setter internally
        self.balance -= amount

        transaction = f"Withdrew {amount}"
        self.transactions.append(f"Withdrew {amount}")

        #Save transaction
        self.save_transaction(transaction)
        print(f"{amount} withdrawn successfully")

    # ============================================
    # 📊 SHOW BALANCE
    # ============================================
    def show_balance(self):
        """
        Uses the getter (self.balance) instead of accessing __balance directly.
        This ensures consistent and controlled access.
        """
        print(f"{self.name}'s balance is: {self.balance}")

    # ============================================
    # 📜 TRANSACTION HISTORY
    # ============================================
    def show_transactions(self):
        print(f"\nTransaction history for {self.name}:")
        for t in self.transactions:
            print("-", t)


# ============================================
# 💼 CHILD CLASS (INHERITANCE)
# ============================================
class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        # Call parent constructor
        super().__init__(name, balance)

        self.interest_rate = interest_rate

    def add_interest(self):
        """
        Demonstrates:
        - Using getter instead of accessing private variable
        - Business logic on top of existing system
        """
        interest = self.balance * (self.interest_rate / 100)

        # This will go through setter validation
        self.balance += interest

        self.transactions.append(f"Interest added {interest}")
        print(f"Interest of {interest} added successfully")


# ============================================
# 🏦 BANK SYSTEM (MANAGES MULTIPLE ACCOUNTS)
# ============================================
class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        """
        Adds a new account to the system.
        """
        self.accounts.append(account)
        print(f"Account created for {account.name}")

    def list_accounts(self):
        """
        Displays all accounts in the system.
        """
        print("\nAll Accounts:")
        for acc in self.accounts:
            print(f"{acc.account_number} - {acc.name}")


# ============================================
# ⚙️ INPUT HANDLING (OUTSIDE THE CLASS)
# ============================================

def get_valid_amount(prompt):
    """
    Handles user input safely.

    WHY OUTSIDE CLASS?
    -------------------
    - Classes should focus on BUSINESS LOGIC
    - Input/output belongs to the interface layer

    This separation is exactly how:
    - Django views work
    - APIs handle requests
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number!")


# ============================================
# 🚀 SYSTEM USAGE
# ============================================

bank = Bank()

account1 = BankAccount("Rashid", 5000)
account2 = SavingsAccount("Kofi", 10000, 5)

bank.create_account(account1)
bank.create_account(account2)

# Perform operations
amount = get_valid_amount("Enter deposit amount for Rashid: ")
account1.deposit(amount)

amount = get_valid_amount("Enter withdrawal amount for Rashid: ")
account1.withdraw(amount)

amount = get_valid_amount("Enter deposit amount for Kofi: ")
account2.deposit(amount)

account2.add_interest()

# Display results
bank.list_accounts()
account1.show_transactions()
account2.show_transactions()