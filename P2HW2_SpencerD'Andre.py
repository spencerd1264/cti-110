# CTI-110

   # P2HW2 - List

   # D'Andre Spencer

   # 10/24/2023

   #
   # Initialize an empty list to store grades
grades = []

# Loop through each module and ask the user to enter the grade
for i in range(1, 7):
    # Ask the user to enter the grade for each module
    grade = float(input("Enter grade for Module {}: ".format(i)))
    # Add the grade to the list
    grades.append(grade)

# Calculate the lowest, highest, sum, and average of grades
lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average_grade = total_grades / len(grades)

# Display the results
print("Lowest Grade: {}".format(lowest_grade))
print("Highest Grade: {}".format(highest_grade))
print("Sum of Grades: {}".format(total_grades))
print("Average Grade: {:.2f}".format(average_grade))
