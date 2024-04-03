# ******************************************************************************************************************
# In Python, dividing by zero raises a ZeroDivisionError. Your task is to create a function that:
# Takes two numbers as arguments.
# Tries to divide the first number by the second number.
# If the second number is zero, it should catch the ZeroDivisionError and return a custom error message.
# If the division is successful, it should return the result.
# Regardless of whether the division is successful or not, it should print a message saying ("Attempted division. "
# "If the inputs are not numbers, it raises a TypeError. It catches this TypeError and returns a custom error message.)
# ******************************************************************************************************************

def divide_numbers(a, b):
    if type(a)!=type(1) or type(b)!=type(1):
        raise TypeError ("not a numbers")

    try:
        result = a / b
        return result
    except ZeroDivisionError as zde:
        print(f"Error: {zde}. Cannot divide by zero.")
        return None
    except TypeError as te:
        print(f"Error: {te}. Inputs must be numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    finally:
        print("Attempted division.")

result1 = divide_numbers(10, 2)
print("Result 1:", result1)

result2 = divide_numbers(5, 0)
print("Result 2:", result2)

result3 = divide_numbers("abc", 2)
print("Result 3:", result3)

