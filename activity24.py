def calculate_grade(average_marks):
    """Calculates the grade based on the average marks."""
    if average_marks >= 90:
        return "A"
    elif average_marks >= 80:
        return "B"
    elif average_marks >= 70:
        return "C"
    elif average_marks >= 60:
        return "D"
    else:
        return "F"

# Input student's name
student_name = input("Enter student's name: ")

# Input marks for each subject
try:
    physics_marks = float(input("Enter marks for Physics: "))
    chemistry_marks = float(input("Enter marks for Chemistry: "))
    biology_marks = float(input("Enter marks for Biology: "))
except ValueError:
    print("Invalid input. Please enter numeric values for marks.")
    exit()

# Calculate total marks and average marks
total_marks = physics_marks + chemistry_marks + biology_marks
average_marks = total_marks / 3

# Determine the grade
grade = calculate_grade(average_marks)

# Display the results
print(f"\nStudent Name: {student_name}")
print(f"Average Marks: {average_marks:.2f}") # Display average with 2 decimal places
print(f"Grade Obtained: {grade}")