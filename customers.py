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

    # Exercise 5 - Lookup table

tier_discounts = {
"bronze": 0,
"silver": 0.05,
"gold": 0.10,
"platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate:.0%}")
print(f"Final Price: ${final_price:.2f}")


# Exercise 6 - List of dictionaries

customers = [
customer,
{"name": "Bob", "tier": "silver", "ytd_spend": 3200},
{"name": "Carol", "tier": "gold", "ytd_spend": 8750}
]

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * rate
    print(f"{person['name']} ({person['tier']}): ${discount_amount:.2f} discount on a $300 purchase")
