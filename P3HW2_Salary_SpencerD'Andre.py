  # CTI-110

   # P3HW2 - Salary

   # D'Andre Spencer

   # 11/7/23

   #
  # Ask user to enter name of employee
employee_name = input("Enter name of employee: ")

# Ask user to enter number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked this week: "))

# Ask user to enter employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate if employee has worked overtime (more than 40 hours)
if hours_worked > 40:
    # Calculate overtime hours
    overtime_hours = hours_worked - 40
    # Calculate overtime pay at 1.5 times the pay rate for each overtime hour
    overtime_pay = overtime_hours * 1.5 * pay_rate
    # Calculate pay for regular hours (40 hours)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    # Calculate pay for regular hours (all hours worked)
    regular_pay = hours_worked * pay_rate

# Calculate gross pay (total amount that should be paid to employee)
gross_pay = regular_pay + overtime_pay

# Display the information with improved formatting
print("\nEmployee Information:")
print("Name:", employee_name)
print("Hours Worked:", hours_worked)
print("Pay Rate: ${:.2f}".format(pay_rate))
print("Overtime Hours:", overtime_hours)
print("Overtime Pay: ${:.2f}".format(overtime_pay))
print("Regular Pay: ${:.2f}".format(regular_pay))
print("Gross Pay: ${:.2f}".format(gross_pay))
