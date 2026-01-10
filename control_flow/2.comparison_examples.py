"""
Comparison Operators in Python

This module demonstrates how comparison operators work in Python.
Examples focus on comparing numbers and understanding boolean results.

Topics covered:
- Equal and not equal comparisons
- Greater than / less than comparisons
- Comparing user input values
- Boolean results of comparison expressions

Author: Muhammet Enes Duran
"""

print("=== Comparison Operators Examples ===")
print("-" * 40)

# =====================
# 1. BASIC COMPARISONS
# =====================

a = 10
b = 20

print("Basic Comparisons:")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")
print(f"a > b  : {a > b}")
print(f"a < b  : {a < b}")
print(f"a >= b : {a >= b}")
print(f"a <= b : {a <= b}")
print("-" * 40)

# ========================
# 2. COMPARING USER INPUT
# ========================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("\nUser Input Comparison:")
print(f"{x} == {y} : {x == y}")
print(f"{x} != {y} : {x != y}")
print(f"{x} > {y}  : {x > y}")
print(f"{x} < {y}  : {x < y}")
print("-" * 40)

# ===============================
# 3. COMPARISON RESULTS (BOOLEAN)
# ===============================

result_1 = x > y
result_2 = x == y

print("Boolean Results:")
print(f"x > y  -> {result_1}")
print(f"x == y -> {result_2}")
print("-" * 40)

print("End of comparison examples.")
