"""
Logical Operators in Python

This module introduces logical operators used to combine
multiple conditions in decision-making processes.

Topics covered:
- and operator
- or operator
- not operator
- Combining logical and comparison expressions
- Simple real-life inspired examples

Author: Muhammet Enes Duran
"""

print("=== LOGICAL OPERATORS ===")
print("-" * 40)

# ================
# 1. AND OPERATOR
# ================
# True only if BOTH conditions are True

a = 10
b = 5
c = 3

print("AND operator examples:")
print(a > b and a > c)   # True
print(b > a and b > c)   # False
print("-" * 40)

# ===============
# 2. OR OPERATOR
# ===============
# True if AT LEAST ONE condition is True

x = 7
y = 12

print("OR operator examples:")
print(x > y or x == 7)   # True
print(x < y or x == 5)   # True
print("-" * 40)

# ================
# 3. NOT OPERATOR
# ================
# Reverses the boolean value

is_raining = False

print("NOT operator examples:")
print(not is_raining)    # True
print("-" * 40)

# =======================
# 4. COMBINED CONDITIONS
# =======================
# Logical operators often work with comparisons

number = int(input("Enter a number: "))

print("\nNumber range check (1 - 100):")
print(number >= 1 and number <= 100)
print("-" * 40)

# ===========================
# 5. SIMPLE REAL-LIFE EXAMPLE
# ===========================
# Login condition simulation

username = input("Username: ")
password = input("Password: ")

print("Login result:")
print(username == "admin" and password == "1234")

print("\nEnd of logical operators module.")
