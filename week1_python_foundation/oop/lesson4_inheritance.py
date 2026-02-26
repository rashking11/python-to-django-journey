# Lesson 4: Inheritance

class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def login(self):
        print(f"{self.name} logged in")


class customer(user):

    def __init__(self, name, email, balance):
        super().__init__(name, email)
        self.balance = balance


class BankStaff(user):


    def __init__(self, name, email, staff_id):
        super().__init__(name, email)
        self.staff_id = staff_id

# Create objects

customer1 = customer("Rashid", "rashking11@gmail.com", 5000)
staff1 = BankStaff("Kofi", "kofi@gmail.com", "STF001")

customer1.login()
staff1.login()

print(customer1.balance)
print(staff1.staff_id)