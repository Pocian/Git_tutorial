Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
Operation = input("Enter operation (+, -, *, /): ")

if Operation == "+":
    Result = Num1 + Num2
elif Operation == "-":
    Result = Num1 - Num2
elif Operation == "*":
    Result = Num1 * Num2
elif Operation == "/":
    Result = Num1 / Num2
else:
    Result = "Invalid operation"

print("Result:", Result)