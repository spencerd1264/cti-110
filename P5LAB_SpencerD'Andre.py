# Define your function here.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_feb(user_year):
    if is_leap_year(user_year):
        return 29
    else:
        return 28

if __name__ == '__main__':
    # Input year from the user
    user_year = int(input())
    
    # Determine the number of days in February for the input year
    result = days_in_feb(user_year)
    
    # Display the result
    print(f"{user_year} has {result} days in February.")








