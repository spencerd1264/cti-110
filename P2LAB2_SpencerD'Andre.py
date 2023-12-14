# Input four floating-point numbers
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output rounded integers
print(f'{product:.0f} {average:.0f}')

# Output floating-point numbers with three digits after the decimal point
print(f'{product:.3f} {average:.3f}')
