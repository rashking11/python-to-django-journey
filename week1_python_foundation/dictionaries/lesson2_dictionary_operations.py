customer = {
    "name": "Rashid",
    "account_number": "ACC1001",
    "balance": 5000
}

print("Original customer record: ")
print(customer)

#Updating customer balance

customer["balance"] = customer["balance"] + 2000
print("\nAfter deposit of 2000:")
print(customer)

#Adding a new key

customer["email"] = "rashking11@gmail.com"
print("\nAfter adding email:")
print(customer)

#Removing a customer
del customer["email"]

print("\nAfter removing customer email:")
print(customer)