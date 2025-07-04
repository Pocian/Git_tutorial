def calculator():

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

while True:
  calculator()
  cont = input("Do you want to perform another calculation? (yes/no): ")
  if cont.lower() != 'yes':
    break
print("Thank you for using the calculator!")
# End of Calculator.py
# This code defines a simple calculator that performs basic arithmetic operations.
# It prompts the user for two numbers and an operation, then displays the result.
# The user can perform multiple calculations until they choose to exit.
# The code is structured to handle invalid operations gracefully.
# The calculator supports addition, subtraction, multiplication, and division.