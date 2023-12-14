''' Type your code here. '''
# Taking inputs for gas mileage and cost of gas
mileage = float(input())
gas_cost = float(input())

# Calculating gas cost for 20 miles, 75 miles, and 500 miles
cost_20_miles = (20 / mileage) * gas_cost
cost_75_miles = (75 / mileage) * gas_cost
cost_500_miles = (500 / mileage) * gas_cost

# Outputting the calculated gas costs with two digits after the decimal point
print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
