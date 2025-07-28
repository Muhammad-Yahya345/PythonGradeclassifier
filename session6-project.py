# 📝 Grades Classifier - Session 6: Data Structures I - Dictionaries
# Welcome to Python School! Let's help you process your exam scores like a pro 📚✨
# We will update our last session's project to allow adding multiple subjects using
# the 'dict' data structure in Python.

# Print welcome message

print("Welcome to Python School! Let's help you process your exam scores like a pro \n")

# Ask for student name

student_name = input("Enter your name: ")

# Define dictionary of subject labels
# The key should be subject name and the value should be the
# label for that subject. For example, math maps to Mathematics ➗

subject_labels = {
    'math': 'Mathematics',
    'science': 'Science',
    'english': 'English'
}

# Define dictionary to store obtained marks in each subject

subject_marks = {}

# Take marks for three subjects (out of 100 each)
# Use a for loop to iterate over the appropriate dictionary.
# You should also define and iteratively update a variable for the
# accumulated obtained marks.

total_obtained = 0
for subject in subject_labels:
    mark = float(input(f"Enter your {subject_labels[subject]} mark (out of 100): "))
    subject_marks[subject] = mark
    total_obtained += mark

# Compute total possible marks assuming each subject is 100 marks.

total_possible = len(subject_labels) * 100

# Calculate average and percentage

average = total_obtained / len(subject_labels)
percentage = (total_obtained / total_possible) * 100

# Round for nicer output

average = round(average, 2)
percentage = round(percentage, 2)

# Print student report

print("\n--- Student Report ---")
print(f"Student Name: {student_name}")
print("\nSubject Scores:")
for subject, mark in subject_marks.items():
    print(f"{subject_labels[subject]}: {mark}/100")

# Display results

print("\n--- Results ---")
print(f"Total Marks Obtained: {total_obtained}/{total_possible}")
print(f"Average Score: {average}")
print(f"Percentage: {percentage}%")

# Assign grade based on percentage

if percentage >= 90:
  grade = 'A'
elif percentage >= 80:
  grade = 'B'
elif percentage >= 70:
  grade = 'C'
elif percentage >= 60:
  grade = 'D'
else:
  grade = 'F'

print(f"\nGrade: {grade}")

# Encouraging message

print("\nKeep working hard and keep learning! \n")

# 💡 Notes for learners:
# - Arithmetic: + for addition, / for division, () controls order (precedence).
# - Comparison: >= checks "greater than or equal to".
# - A comparison returns True or False, which we can print as a result. Have fun.