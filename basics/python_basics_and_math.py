"""
Python Basics and Math Operations

This file demonstrates fundamental Python concepts:
- Variables and data types
- Type checking
- User input and type conversion
- Basic arithmetic operations
- Simple geometry calculations (area & perimeter)

Author: Muhammet Enes Duran
"""

# =========================
# 1. COMMENTS & VARIABLES
# =========================

# This is a comment line. Comments are not executed by Python.

x = 10                  # Integer
y = 12.5                # Float
name = "Menes"          # String
is_active = True        # Boolean

print("Variable Values:")
print(x, y, name, is_active)
print("-" * 30)

# =========================
# 2. DATA TYPES & TYPE CHECKING
# =========================

print("Data Types:")
print(type(x))
print(type(y))
print(type(name))
print(type(is_active))
print("-" * 30)

# Python allows dynamic typing
x = "Barış Manço"
print("Updated x:", x)
print("New type of x:", type(x))
print("-" * 30)

# ===============================
# 3. USER INPUT & TYPE CONVERSION
# ===============================

# Input values are always strings
number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))

total = number1 + number2

print(f"{number1} + {number2} = {total}")
print("-" * 30)

# ==============================
# 4. BASIC ARITHMETIC OPERATIONS
# ==============================

a = 15
b = 4

print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("-" * 30)

# =========================
# 5. GEOMETRY CALCULATIONS
# =========================

# Square
side = float(input("Enter side length of square: "))
square_area = side ** 2
square_perimeter = 4 * side

print(f"Square Area: {square_area}")
print(f"Square Perimeter: {square_perimeter}")
print("-" * 30)

# Rectangle
short_edge = float(input("Enter short edge of rectangle: "))
long_edge = float(input("Enter long edge of rectangle: "))

rectangle_area = short_edge * long_edge
rectangle_perimeter = 2 * (short_edge + long_edge)

print(f"Rectangle Area: {rectangle_area}")
print(f"Rectangle Perimeter: {rectangle_perimeter}")
print("-" * 30)

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

triangle_area = (base * height) / 2
print(f"Triangle Area: {triangle_area}")

print("\nEnd of Python Basics and Math Operations")



