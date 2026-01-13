"""
Comparison Practice – Python Control Flow

This file focuses on comparison operators in Python
and how they are used inside decision structures.

Focus:
- ==, !=
- <, <=, >, >=
- Comparing numbers and strings
- Real-life inspired examples

Author: Muhammet Enes Duran
"""

# ======================
# 1. NUMBER COMPARISON
# ======================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater.")
elif a < b:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")

print("-" * 40)

# ==================
# 2. EQUALITY CHECK
# ==================

username = input("Enter username: ")

if username == "admin":
    print("Welcome admin.")
else:
    print("Unknown user.")

print("-" * 40)

# =========================
# 3. PASSWORD LENGTH CHECK
# =========================

password = input("Enter password: ")

if len(password) < 6:
    print("Password is too short.")
elif len(password) <= 10:
    print("Password length is acceptable.")
else:
    print("Password is strong.")

print("-" * 40)

# ====================
# 4. GRADE COMPARISON
# ====================

score = int(input("Enter exam score: "))

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")

print("-" * 40)
print("End of comparison practice.")

