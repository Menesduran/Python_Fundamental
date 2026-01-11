"""
Mini Projects – Control Flow in Python

This module contains small, practical projects that combine
core control flow concepts learned so far.

Concepts used:
- if / elif / else
- comparison operators
- logical operators
- nested conditions
- guard conditions
- match-case statements

These mini projects aim to reinforce decision-making logic
without introducing functions or advanced structures.

Author: Muhammet Enes Duran
"""

print("=== Mini Projects: Control Flow ===")
print("=" * 50)

# ======================================
# 1. EVEN / ODD NUMBER CHECK WITH GUARD
# ======================================

number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers are not allowed.")
else:
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

print("-" * 50)

# =======================
# 2. SIMPLE LOGIN SYSTEM
# =======================

username = input("Username: ")
password = input("Password: ")

if username != "admin" or password != "1234":
    print("Login failed.")
else:
    print("Login successful.")

print("-" * 50)

# ==========================
# 3. EXAM RESULT EVALUATION
# ==========================

score = int(input("Enter exam score: "))

if score < 0 or score > 100:
    print("Invalid score.")
else:
    if score >= 85:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Failed.")

print("-" * 50)

# ====================================
# 4. PRODUCT CATEGORY USING MATCH-CASE
# ====================================

product = input("Enter product name: ").lower()

match product:
    case "apple" | "banana" | "spinach":
        print("Go to the grocery section.")
    case "shampoo" | "soap" | "perfume":
        print("Go to the cosmetics section.")
    case "phone" | "tablet" | "notebook":
        print("Go to the technology section.")
    case _:
        print("Product not found.")

print("-" * 50)

# ========================
# 5. SPEED CONTROL SYSTEM
# ========================

vehicle_type = input("Enter vehicle type (car / truck / motorcycle): ").lower()
speed = int(input("Enter speed: "))

if speed <= 0:
    print("Speed must be positive.")
else:
    match vehicle_type:
        case "car":
            print("Penalty applied." if speed >= 60 else "No penalty.")
        case "truck":
            print("Penalty applied." if speed >= 30 else "No penalty.")
        case "motorcycle":
            print("Penalty applied." if speed >= 70 else "No penalty.")
        case _:
            print("Invalid vehicle type.")

print("=" * 50)

# =====================
# 6. USER REGISTRATION
# =====================

username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

if not username:
    print("Username cannot be empty.")
elif len(password) < 6:
    print("Password must be at least 6 characters long.")
elif age < 18:
    print("You must be at least 18 years old to register.")
else:
    print("Registration completed successfully!")

print("-" * 50)

# ================
# 7. ATM MENU
# ================

balance = 1000

print("""
1 - Check Balance
2 - Deposit Money
3 - Withdraw Money
0 - Exit
""")

choice = int(input("Select an option: "))

match choice:
    case 1:
        print(f"Current balance: {balance} TL")
    case 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"New balance: {balance} TL")
    case 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Remaining balance: {balance} TL")
    case 0:
        print("Exiting the system...")
    case _:
        print("Invalid selection!")

print("-" * 50)
print("End of mini projects.")
