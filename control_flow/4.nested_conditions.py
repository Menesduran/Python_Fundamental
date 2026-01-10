"""
Nested Conditions in Python

This module demonstrates the use of nested if-else structures
to evaluate multiple dependent conditions.

Topics covered:
- Nested if statements
- Dependent condition checks
- Readability concerns in nested structures
- Simple real-life examples

Author: Muhammet Enes Duran
"""

print("=== Nested Conditions ===")
print("-" * 40)

# ===================
# 1. BASIC NESTED IF
# ===================

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are also a senior citizen.")
else:
    print("You are under 18.")

print("-" * 40)

# ========================
# 2. LOGIN CHECK (NESTED)
# ========================

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")

print("-" * 40)

# =========================
# 3. NUMBER CLASSIFICATION
# =========================

number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("Number is zero.")
    else:
        print("Number is positive.")
else:
    print("Number is negative.")

print("End of nested condition examples.")
