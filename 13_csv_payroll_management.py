# CSV-based payroll management system
import csv
from pathlib import Path

CSV_FILE = Path("payroll.csv")
FIELDS = ["employee_id", "name", "basic_salary", "allowance", "deduction", "net_salary"]

if not CSV_FILE.exists():
    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=FIELDS).writeheader()

while True:
    print("\\n1. Add employee payroll  2. View payroll  3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee name: ")
        basic = float(input("Basic salary: "))
        allowance = float(input("Allowance: "))
        deduction = float(input("Deduction: "))
        net = basic + allowance - deduction

        row = {
            "employee_id": emp_id,
            "name": name,
            "basic_salary": f"{basic:.2f}",
            "allowance": f"{allowance:.2f}",
            "deduction": f"{deduction:.2f}",
            "net_salary": f"{net:.2f}"
        }
        with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writerow(row)
        print(f"Payroll saved. Net salary = {net:.2f}")

    elif choice == "2":
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                print(row)

    elif choice == "3":
        break
    else:
        print("Invalid choice.")
