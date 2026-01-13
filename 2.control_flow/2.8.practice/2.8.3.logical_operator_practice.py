"""
Logical Operators Practice – Python Control Flow

This file contains practice exercises for logical operators
used in decision-making structures.

Focus:
- and / or / not
- Combining multiple conditions
- Real-life inspired validation logic

Author: Muhammet Enes Duran
"""

print("=== Logical Operators Practice ===")
print("=" * 45)

# ====================
# 1. LOGIN VALIDATION
# ====================

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login successful.")
else:
    print("Invalid credentials.")

print("-" * 45)

# ========================
# 2. AGE PERMISSION CHECK
# ========================

age = int(input("Enter your age: "))

if age >= 18 and age <= 65:
    print("You are allowed.")
else:
    print("You are not allowed.")

print("-" * 45)

# =================
# 3. WEEKEND CHECK
# =================

day = input("Enter day: ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend.")
else:
    print("It's a weekday.")

print("-" * 45)

# =======================
# 4. INVALID INPUT GUARD
# =======================

value = input("Enter a value: ")

if not value:
    print("Input cannot be empty.")
else:
    print("Input accepted.")

print("-" * 45)

# =====================
# 5. SCORE RANGE CHECK
# =====================

score = int(input("Enter score: "))

if not (score < 0 or score > 100):
    print("Score is valid.")
else:
    print("Invalid score.")

print("=" * 45)
print("End of logical operator practice.")

