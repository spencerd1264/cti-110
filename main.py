# Get the first user input and store it in user_num
user_num = int(input('Enter integer:\n'))

# Output the user's input
print(f'You entered: {user_num}')

# Calculate and output the square and cube of the user's input
user_num_squared = user_num * user_num
user_num_cubed = user_num * user_num * user_num
print(f'{user_num} squared is {user_num_squared}')
print(f'And {user_num} cubed is {user_num_cubed} !!')

# Get the second user input and store it in user_num2
user_num2 = int(input('Enter another integer:\n'))

# Calculate and output the sum and product of user_num and user_num2
sum_result = user_num + user_num2
product_result = user_num * user_num2
print(f'{user_num} + {user_num2} is {sum_result}')
print(f'{user_num} * {user_num2} is {product_result}')
