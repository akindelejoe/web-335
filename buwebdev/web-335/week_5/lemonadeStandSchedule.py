"""
Author: Joe Akindele
Date: 2025-06-29
File Name: akindele_lemonadeStandSchedule.py
Description: This program manages a weekly lemonade stand schedule using lists, conditionals, and loops.
"""

# List of 5 tasks to running a lemonade stand
tasks = [
    "Buy lemons and sugar",
    "Prepare lemonade mix",
    "Set up the stand",
    "Sell lemonade to customers",
    "Clean up the stand"
]

# Display all tasks using a for loop
print("Lemonade Stand Tasks for the Week ")
for task in tasks:
    print(f"- {task}")

print("\n Weekly Schedule:\n")

# List of days from Sunday to Saturday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off. Time to rest and recharge! ")
    else:
        task = tasks[i % len(tasks)]
        print(f"{day}: Task - {task}")
