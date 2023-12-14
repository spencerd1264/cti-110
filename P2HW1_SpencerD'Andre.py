# This will help manage your budget for Vacation

   # 10/19/2023

   # CTI-110 P2HW1 - Travel

   # D'Andre Spencer

   #
 # Step 1: Ask user to enter their budget
budget = float(input("Enter your budget: $"))

# Step 2: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask user how much they think gas will cost
gas_estimate = float(input("How much do you think gas will cost? $"))

# Step 4: Ask user how much they will need for accommodation
accommodation_estimate = float(input("How much will you need for accommodation? $"))

# Step 5: Ask user how much food will cost
food_estimate = float(input("How much will food cost? $"))

# Step 6: Add estimated expenses
total_estimated_expenses = gas_estimate + accommodation_estimate + food_estimate

# Step 7: Subtract estimated expenses from budget
remaining_budget = budget - total_estimated_expenses

# Step 8: Display results with nicely aligned output
print("\nTravel Details:")
print(f"{'Destination:':<25} {destination}")
print(f"{'Budget:':<25} ${budget:.2f}")
print(f"{'Estimated Gas Expense:':<25} ${gas_estimate:.2f}")
print(f"{'Estimated Accommodation Expense:':<25} ${accommodation_estimate:.2f}")
print(f"{'Estimated Food Expense:':<25} ${food_estimate:.2f}")
print(f"{'Total Estimated Expenses:':<25} ${total_estimated_expenses:.2f}")
print(f"{'Remaining Budget:':<25} ${remaining_budget:.2f}")
  
