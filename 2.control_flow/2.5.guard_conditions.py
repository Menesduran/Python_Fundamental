"""
Guard Conditions in Python

This module demonstrates the concept of guard conditions in control flow.
Guard conditions are used to handle invalid or undesired cases early,
allowing the main logic to remain clean and readable.

Topics covered:
- What guard conditions are
- Input validation using guards
- Range checks with early exits
- Reducing nested if-else structures
- Comparing nested conditions vs guard conditions

Author: Muhammet Enes Duran
"""

print("=== Guard Conditions ===")
print("-" * 40)

# =========================
# 1. BASIC GUARD CONDITION
# =========================

number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers are not allowed.")
else:
    print(f"Valid number entered: {number}")

print("-" * 40)

# ===============
# 2. RANGE GUARD
# ===============

age = int(input("Enter your age: "))

if age <= 0 or age > 120:
    print("Invalid age value.")
else:
    print("Age accepted.")

print("-" * 40)

# ===============================
# 3. LOGIN VALIDATION WITH GUARD
# ===============================

username = input("Username: ")
password = input("Password: ")

if username != "admin" or password != "1234":
    print("Access denied.")
else:
    print("Login successful.")

print("-" * 40)

# ===============================
# 4. GUARD VS NESTED (COMPARISON)
# ===============================

score = int(input("Enter exam score: "))

# Guard approach
if score < 0 or score > 100:
    print("Invalid score.")
else:
    if score >= 50:
        print("Passed.")
    else:
        print("Failed.")

print("-" * 40)

print("End of guard condition examples.")
