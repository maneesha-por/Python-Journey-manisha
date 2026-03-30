# --- Day 01: Python Basics for Volt Project ---

# 1. Output - Displaying messages
print("Hello World!")
print("Welcome to Manisha's Volt Project.")

# 2. Variables - Storing business data
user_name = "Manisha"
business_name = "Volt Ecosystem"
shares = 1000
battery_level = 95

# 3. Arithmetic Operations - Calculations
# Addition
total_shares = shares + 500
print("Total Shares after bonus:")
print(total_shares)

# Subtraction
usage = 10
remaining_battery = battery_level - usage
print("Remaining Battery Level:")
print(remaining_battery)

# Multiplication
card_price = 500
cards_sold = 5
total_income = card_price * cards_sold
print("Total Income from Sales:")
print(total_income)

# Division
budget = 1000
parts_count = 4
cost_per_part = budget / parts_count
print("Cost per Part:")
print(cost_per_part)

# 4. Decision Making - Logic for the Chip
if battery_level < 20:
    print("Alert: Low Battery!")
else:
    print("Status: Battery OK")

# 5. Logic for Investors
my_shares = 150
if my_shares > 100:
    print("Role: You are a Big Boss")
else:
    print("Role: Keep Working")
