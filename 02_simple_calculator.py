# Simple calculator
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        result = "Cannot divide by zero"
    else:
        result = a / b
else:
    result = "Invalid operator"

print("Result:", result)
