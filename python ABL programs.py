1. Case Study 2: Progressive Electricity Billing
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 100 * 1.50 + (units - 100) * 2.50
    else:
        energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

    fixed_charge = 50
    total = energy_charge + fixed_charge

    print(f"Energy charge: Rs. {energy_charge:.2f}")
    print(f"Fixed charge: Rs. {fixed_charge:.2f}")
    print(f"Total bill: Rs. {total:.2f}")

2. Case Study 4: Employee Payroll and Deduction Analysis
basic = float(input("Enter basic pay: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime pay: "))

if basic < 0 or allowance < 0 or overtime < 0:
    print("Invalid amount")
else:
    gross = basic + allowance + overtime
    deduction = gross * 0.10
    net_salary = gross - deduction

    print(f"Gross salary: Rs. {gross:.2f}")
    print(f"Deduction (10%): Rs. {deduction:.2f}")
    print(f"Net salary: Rs. {net_salary:.2f}")

3. Case Study 7: Retail Billing with Discount
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

if quantity < 0 or price < 0:
    print("Invalid quantity or price")
else:
    subtotal = quantity * price

    if subtotal >= 1000:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_amount = subtotal - discount

    print("Product:", product)
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Final amount: Rs. {final_amount:.2f}")

4. Case Study 11: Examination Result and Pass Validation
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

if any(mark < 0 or mark > 100 for mark in [m1, m2, m3]):
    print("Invalid marks")
else:
    total = m1 + m2 + m3
    average = total / 3

    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    print(f"Total marks: {total:.0f}/300")
    print(f"Average: {average:.2f}")
    print("Result:", result)

5. Case Study 12: Attendance Recovery Computation
attended = int(input("Enter classes attended: "))
held = int(input("Enter total classes held: "))

if attended < 0 or held < 0 or attended > held or held == 0:
    print("Invalid attendance data")
else:
    percentage = attended / held * 100
    future = 0

    while (attended + future) / (held + future) * 100 < 75:
        future += 1

    print(f"Current attendance: {percentage:.2f}%")
    print("Additional classes to attend:", future)
    print(
        f"Attendance after those classes: "
        f"{(attended + future) / (held + future) * 100:.2f}%")

6. Case Study 13: ATM Transaction Sequence Simulation
balance = 1000.0
successful = 0

count = int(input("How many transactions? "))

for i in range(count):
    kind = input("Transaction type (D/W): ").upper()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive")

    elif kind == "D":
        balance += amount
        successful += 1
        print("Deposit successful")

    elif kind == "W":
        if amount <= balance:
            balance -= amount
            successful += 1
            print("Withdrawal successful")
        else:
            print("Rejected: insufficient balance")

    else:
        print("Rejected: invalid transaction type")

print(f"Final balance: Rs. {balance:.2f}")
print("Successful transactions:", successful)

7. Case Study 27: Numeric Pattern Generator
height = int(input("Enter pyramid height (1-9): "))

if height < 1 or height > 9:
    print("Invalid height")
else:
    for row in range(1, height + 1):
        print(" " * (height - row), end="")

        for number in range(1, row + 1):
            print(number, end="")

        print()

8. Case Study 29: Password Policy Validation
password = input("Enter a sample password: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters")

if not any(ch.isupper() for ch in password):
    errors.append("Add an uppercase letter")

if not any(ch.islower() for ch in password):
    errors.append("Add a lowercase letter")

if not any(ch.isdigit() for ch in password):
    errors.append("Add a digit")

if not any(not ch.isalnum() for ch in password):
    errors.append("Add a special character")

if not errors:
    print("Password meets all rules")
else:
    print("Password does not meet the rules:")

    for error in errors:
        print("-", error)

9. Case Study 42: Student Marks Matrix Analysis
students = ["Asha", "Bala", "Charan"]

marks = [
    [80, 75, 90],
    [65, 88, 72],
    [92, 91, 89]
]

totals = []

for row in marks:
    totals.append(sum(row))

for i in range(len(students)):
    average = totals[i] / len(marks[i])
    print(
        f"{students[i]}: Total = {totals[i]}, "
        f"Average = {average:.2f}"
    )

top_index = totals.index(max(totals))

print("Top performer:", students[top_index])
print("Highest total:", totals[top_index])

10. Case Study 49: Tuple-Based Product Catalogue Audit
products = [
    ("P101", 120.0, 10),
    ("P102", 75.0, 3),
    ("P103", 250.0, 4),
    ("P104", 40.0, 12)
]

minimum_stock = 5
replenish = []

for product_id, price, stock in products:
    value = price * stock

    print(
        f"{product_id}: Stock value = Rs. {value:.2f}, "
        f"Stock = {stock}"
    )

    if stock < minimum_stock:
        replenish.append(product_id)

print("Products to replenish:", ", ".join(replenish))
