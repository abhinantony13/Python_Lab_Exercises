# Area calculation
print("1. Circle\n2. Rectangle\n3. Triangle")
choice = input("Choose a shape (1-3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius * radius
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
else:
    area = None
    print("Invalid choice")

if area is not None:
    print("Area =", area)
