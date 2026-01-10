"""
decision_basics.py

This file demonstrates basic decision-making mechanisms in Python.
It introduces if / elif / else statements using simple, beginner-friendly examples.

Covered topics:
- Even / odd number check
- Comparing two numbers
- Number sign detection (positive / negative / zero)
- Basic conditional logic with user input

Author: Muhammet Enes Duran
"""

# --------------------------------------------------
# Example 1: Even or Odd Number Check
# --------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print("-" * 40)

# --------------------------------------------------
# Example 2: Compare Two Numbers
# --------------------------------------------------

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(f"{x} is greater than {y}.")
elif x < y:
    print(f"{y} is greater than {x}.")
else:
    print("Both numbers are equal.")

print("-" * 40)

# --------------------------------------------------
# Example 3: Number Sign Detection
# --------------------------------------------------

value = int(input("Enter a number: "))

if value > 0:
    print("Positive number.")
elif value < 0:
    print("Negative number.")
else:
    print("Zero.")

print("-" * 40)

# --------------------------------------------------
# Example 4: Season to Months Mapping
# --------------------------------------------------

season = input("Enter a season: ").lower()

if season == "kış":
    print("Aralık - Ocak - Şubat")
elif season == "ilkbahar":
    print("Mart - Nisan - Mayıs")
elif season == "yaz":
    print("Haziran - Temmuz - Ağustos")
elif season == "sonbahar":
    print("Eylül - Ekim - Kasım")
else:
    print("Invalid season input.")

