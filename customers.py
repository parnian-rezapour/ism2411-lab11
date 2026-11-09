# Reflection 1:
# I would use .get() when a field might be missing, such as an optional
# customer email address. I would use bracket notation for required fields
# because a missing key should alert me that something is wrong.

# Reflection 2:
# Summarizing sales by region reminds me of using SUMIF or a PivotTable
# in Excel. Python could be useful for large datasets because I could
# repeat the calculation automatically without rebuilding formulas.

# Exercise 1 - One customer

customer = {
"name": "Alice",
"email": "alice@example.com",
"tier": "gold",
"ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 - Update and add

customer["phone"] = "555-5555"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 - Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)


# Exercise 4 - Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop returns only the keys, not key-value pairs.
for key in customer:
    print(key)