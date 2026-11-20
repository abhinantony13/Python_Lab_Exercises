# Student grading system
students = []

count = int(input("How many students? "))
for _ in range(count):
    name = input("Student name: ")
    marks = []
    for subject in range(1, 4):
        marks.append(float(input(f"Enter mark for subject {subject} (0-100): ")))

    average = sum(marks) / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    students.append({"name": name, "average": average, "grade": grade})

print("\\nSTUDENT RESULTS")
for student in students:
    print(f"{student['name']}: Average = {student['average']:.2f}, Grade = {student['grade']}")
