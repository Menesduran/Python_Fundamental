"""
Match-Case Statements in Python

This module demonstrates the usage of the match-case statement,
introduced in Python 3.10, as a cleaner alternative to long
if-elif-else chains.

Topics covered:
- Basic match-case syntax
- Matching string values
- Default case handling
- Comparison with if-elif structure
- Simple real-life examples

Author: Muhammet Enes Duran
"""

print("=== Match-Case Examples ===")
print("-" * 40)

# ===================
# 1. BASIC MATCH-CASE
# ===================

day = input("Enter a day: ").lower()

match day:
    case "monday":
        print("Start of the work week.")
    case "friday":
        print("Almost weekend!")
    case "saturday" | "sunday":
        print("Weekend time.")
    case _:
        print("Invalid day.")

print("-" * 40)

# ==================
# 2. SEASON EXAMPLE
# ==================

season = input("Enter a season: ").lower()

match season:
    case "winter":
        print("December - January - February")
    case "spring":
        print("March - April - May")
    case "summer":
        print("June - July - August")
    case "autumn":
        print("September - October - November")
    case _:
        print("Unknown season.")

print("-" * 40)

# =========================
# 3. SIMPLE MENU SELECTION
# =========================

choice = input("Choose an option (add / delete / update): ").lower()

match choice:
    case "add":
        print("Item added.")
    case "delete":
        print("Item deleted.")
    case "update":
        print("Item updated.")
    case _:
        print("Invalid choice.")

print("-" * 40)

# =========================
# 4. MATCH-CASE VS IF-ELIF
# =========================

status_code = int(input("Enter status code (200, 404, 500): "))

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status code.")

print("-" * 40)
print("End of match-case examples.")
