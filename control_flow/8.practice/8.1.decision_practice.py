"""
Decision Practice – Python Control Flow

This file contains practice exercises for basic decision-making
using if / elif / else statements and guard conditions.

Focus:
- User input validation
- Simple decision logic
- Real-life inspired examples

Author: Muhammet Enes Duran
"""

print("=== Decision Practice ===")
print("=" * 40)

# ==============================
# 1. POSITIVE / NEGATIVE / ZERO
# ==============================

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("-" * 40)

# ======================
# 2. AGE CHECK (GUARD)
# ======================

age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age < 18:
    print("You are under 18.")
else:
    print("You are allowed.")

print("-" * 40)

# =====================
# 3. EVEN / ODD CHECK
# =====================

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")

print("-" * 40)

# =========================
# 4. SIMPLE PASSWORD CHECK
# =========================

password = input("Enter password: ")

if password == "":
    print("Password cannot be empty.")
elif password == "python123":
    print("Access granted.")
else:
    print("Access denied.")

print("-" * 40)

# =====================
# 5. SHOPPING DISCOUNT
# =====================

amount = float(input("Enter total shopping amount: "))

if amount <= 0:
    print("Invalid amount.")
elif amount >= 1000:
    print("You get a 20% discount.")
elif amount >= 500:
    print("You get a 10% discount.")
else:
    print("No discount applied.")

print("=" * 40)
print("End of decision practice.")
