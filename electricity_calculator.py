# Electricity Bill Calculator
RATE = 12.90

# validate customer name
while True:
    name = input("Enter customer name: ").strip()

    if name.strip() != "":
        break
    else:
        print("Customer name is required.")

# validate previous meter reading
while True:
    previous = float(input("Enter previous meter reading: "))

    if previous == 0 or previous > 0:
        break
    else:
        print("Enter a valid previous meter reading, it must be greater than or equal to 0.")

# validate current meter reading
while True:
    current = float(input("Enter current meter reading: "))

    if current >= previous:
        break
    else:
        print("Enter a valid current meter reading, it must be greater than or equal to the previous meter reading.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
