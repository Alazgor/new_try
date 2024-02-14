def calculate_operations(num1, num2):
    try:
        # Attempting to convert input to float
        num1 = float(num1)
        num2 = float(num2)

        # Performing operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Handling division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            division = num1 / num2

        return addition, subtraction, multiplication, division

    except ValueError:
        raise ValueError("Error: Please enter valid numeric input.")

    except Exception as e:
        raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    # Taking user input
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Calculating operations and handling errors
        result = calculate_operations(num1, num2)

        # Displaying the result
        print("\nResult:")
        print(f"Sum: {result[0]}")
        print(f"Subtraction: {result[1]}")
        print(f"Multiplication: {result[2]}")
        print(f"Division: {result[3]}")

    except ValueError as ve:
        print(ve)

    except ZeroDivisionError as zde:
        print(zde)

    except Exception as e:
        print(e)
