#Lesson 3: Nested dictionaries

customers = {
    "COO1": { 
        "name": "Rashid",
        "balance": 5000
    },

    "C002": {
        "name": "Kofi",
        "balance": 3000

    }
}

print("All customers:")
print(customers)

#Access Rashid's balance
print("\nRashid's balance")
print(customers["COO1"]["balance"])

#Deposit 1000 into Kofi's Account
customers["C002"]["balance"] += 1000

#Balance after depositing 1000 into Kofi's account

print(customers["C002"])