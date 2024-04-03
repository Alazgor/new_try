# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc..
# Initiate class and show up some calculations.

class Calculator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

# Input values for num1 and num2
a = float(input("Enter the first number (num1): "))
b = float(input("Enter the second number (num2): "))

# Create an instance of the Calculator class
acalc = Calculator(a, b)

# Perform addition and print the result
result_add = acalc.add()
print(f"Addition: {a} + {b} = {result_add}")

# You can perform similar operations for subtraction, multiplication, and division
result_subtract = acalc.subtract()
print(f"Subtraction: {a} - {b} = {result_subtract}")

result_multiply = acalc.multiply()
print(f"Multiplication: {a} * {b} = {result_multiply}")

result_divide = acalc.divide()
print(f"Division: {a} / {b} = {result_divide}")

