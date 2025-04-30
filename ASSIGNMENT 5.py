# Task 1: Create a Dictionary of Student Marks
student_marks = {
    "Alice": 75,
    "Boby": 95,
    "Caran": 28,
    "Dia": 52,
    "Ram": 68 }
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(student_name,"'s marks:",student_marks[student_name])
else:
    print("Student Not Found")


# Task 2: Demonstrate List Slicing
numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_first_five = first_five[::-1]
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_first_five)
