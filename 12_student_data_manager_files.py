# Student data manager using files
import json
from pathlib import Path

DATA_FILE = Path("students.json")

def load_students():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Data file is invalid. Starting with an empty list.")
    return []

def save_students(students):
    DATA_FILE.write_text(json.dumps(students, indent=4), encoding="utf-8")

students = load_students()

while True:
    print("\\n1. Add student  2. View students  3. Search  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        student = {
            "roll_no": input("Roll number: "),
            "name": input("Name: "),
            "course": input("Course: ")
        }
        students.append(student)
        save_students(students)
        print("Student saved.")
    elif choice == "2":
        if not students:
            print("No student records.")
        for student in students:
            print(student)
    elif choice == "3":
        roll = input("Enter roll number: ")
        matches = [s for s in students if s["roll_no"] == roll]
        print(matches if matches else "Student not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
