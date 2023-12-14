
# CTI-110
 # P3HW1 - List
 
 # D'Andre Spencer
 
 # 11/2/2023
 
 #


# This program takes a number grade, determines average, and displays a letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: Determine lowest, highest, sum, and average for grades
lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average_grade = total_grades / len(grades)

# Display the results
print("Lowest Grade: {}".format(lowest_grade))
print("Highest Grade: {}".format(highest_grade))
print("Sum of Grades: {}".format(total_grades))
print("Average Grade: {:.2f}".format(average_grade))

# Determine letter grade for average
if average_grade >= 90:
    print('Your grade is: A')
elif average_grade >= 80:
    print('Your grade is: B')
elif average_grade >= 70:
    print('Your grade is: C')
elif average_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

