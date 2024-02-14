# main.py
from calculator import addition, subtraction, multiplication, division

# Example usage:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result_addition = addition(num1, num2)
    result_subtraction = subtraction(num1, num2)
    result_multiplication = multiplication(num1, num2)
    result_division = division(num1, num2)

    print("\nResult:")
    print(f"Addition: {result_addition}")
    print(f"Subtraction: {result_subtraction}")
    print(f"Multiplication: {result_multiplication}")
    print(f"Division: {result_division}")

except ValueError as ve:
    print(f"Error: {ve}")

except ZeroDivisionError as zde:
    print(zde)

except Exception as e:
    print(f"An error occurred: {e}")
