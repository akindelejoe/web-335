"""
Author: Joseph Akindele
Date: June 16, 2025
File Name: akindele_lemonadeStand.py
Description: This program calculates the cost and profit of making lemonade using functions.
"""

# Function to calculate total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost  # Summing cost of lemons and sugar
    return total_cost  # Returning total cost

# Function to calculate profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Reusing the cost function
    profit = selling_price - total_cost  # Subtracting cost from selling price
    return profit  # Returning the calculated profit

# Test variables
lemons_cost = 4.00
sugar_cost = 2.00
selling_price = 10.00

# Output strings
cost_output = "Lemons: $" + str(lemons_cost) + " + Sugar: $" + str(sugar_cost) + " = Total Cost: $" + str(calculate_cost(lemons_cost, sugar_cost))
profit_output = "Selling Price: $" + str(selling_price) + " - Total Cost: $" + str(calculate_cost(lemons_cost, sugar_cost)) + " = Profit: $" + str(calculate_profit(lemons_cost, sugar_cost, selling_price))

# Printing results
print(cost_output)
print(profit_output)
