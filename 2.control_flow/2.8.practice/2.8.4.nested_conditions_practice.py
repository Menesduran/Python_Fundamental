"""
Nested Conditions Practice – Python Control Flow

This file contains practice exercises using nested if-else statements.
It demonstrates scenarios where nested logic is common and
how guard conditions can simplify complex structures.

Focus:
- if inside if
- Decision trees
- Readability and structure

Author: Muhammet Enes Duran
"""

print("=== Nested Conditions Practice ===")
print("=" * 50)

# =========================
# 1. EXAM RESULT SYSTEM
# =========================

score = int(input("Enter exam score: "))

if score >= 0 and score <= 100:
    if score >= 50:
        print("You passed the exam.")
        if score >= 85:
            print("Grade: Excellent")
        else:
            print("Grade: Pass")
    else:
        print("You failed the exam.")
else:
    print("Invalid score.")

# Classic nested approach:
# - Works correctly
# - Hard to read and maintain as conditions grow

print("-" * 50)

# =========================
# 2. LOGIN & ROLE CHECK
# =========================

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    role = input("Enter role (admin/user): ")
    if role == "admin":
        print("Welcome admin.")
    else:
        print("Welcome user.")
else:
    print("Login failed.")

print("-" * 50)

# =========================
# 3. SHOPPING SYSTEM (NESTED)
# =========================

amount = float(input("Enter shopping amount: "))

if amount > 0:
    if amount >= 1000:
        print("20% discount applied.")
    else:
        if amount >= 500:
            print("10% discount applied.")
        else:
            print("No discount.")
else:
    print("Invalid amount.")

print("-" * 50)

# =========================
# 4. SHOPPING SYSTEM (GUARD)
# =========================

amount = float(input("Enter shopping amount: "))

if amount <= 0:
    print("Invalid amount.")
elif amount >= 1000:
    print("20% discount applied.")
elif amount >= 500:
    print("10% discount applied.")
else:
    print("No discount.")

# Guard conditions:
# Same logic as above, but clearer and flatter structur

print("=" * 50)
print("End of nested conditions practice.")
