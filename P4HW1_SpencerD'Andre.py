   # CTI-110

   # P4HW1 - Score List

   # Your Name

   # Date

   #

# Ask the user for the number of scores
num_scores = int(input("How many scores would you like to enter? "))

scores = []  # List to store valid scores

# Loop to collect and validate scores
for i in range(num_scores):
    while True:
        try:
            score = int(input(f"Enter score #{i + 1} (0-100): "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Display lowest score
lowest_score = min(scores)
print(f"\nLowest score entered: {lowest_score}")

# Remove the lowest score from the list
scores.remove(lowest_score)

# Display the modified score list
print("Score List after dropping lowest score:", scores)

# Calculate and display the average of scores in the modified list
average_score = sum(scores) / len(scores)
print("Average of scores in modified list:", average_score)

# Determine letter grade for the average
if 90 <= average_score <= 100:
    grade = 'A'
elif 80 <= average_score < 90:
    grade = 'B'
elif 70 <= average_score < 80:
    grade = 'C'
elif 60 <= average_score < 70:
    grade = 'D'
else:
    grade = 'F'

# Display the letter grade
print("Letter grade for the calculated average:", grade)

