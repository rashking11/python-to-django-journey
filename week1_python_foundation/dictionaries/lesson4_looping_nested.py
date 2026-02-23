customers = {
    "COO1": {"name": "Rashid", "balance": 5000},
    "C002": {"name": "Kofi", "balance": 3000},
    "C003": {"name": "Ama", "balance": 7000}
}

print("Customer Summary:\n")

for customer_id, details in customers.items():
    print("CUSTOMER ID: ", customer_id)
    print("Name: ", details["name"])
    print("Balance: ", details["balance"])
    print("_" * 30)