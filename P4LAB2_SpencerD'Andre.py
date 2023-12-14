def print_increment_range(start, end):
    if end < start:
        print("Second integer can't be less than the first.")
    else:
        current_value = start

        while current_value <= end:
            print(current_value, end=" ")
            current_value += 5

        print()

# Hardcoded input values
first_integer = int(input())
second_integer = int(input())

# Calling the function
print_increment_range(first_integer, second_integer)
