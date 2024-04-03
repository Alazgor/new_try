# 3. Write a decorator that decorates a function which only allows to give write numbers (int or float). Write some functions
# which work with numbers and test your implementation
def check_numbers(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)):
            raise ValueError("First argument must be an integer or a float.")
        if not isinstance(b, (int, float)):
            raise ValueError("Second argument must be an integer or a float.")
        return func(a, b)
    return wrapper

@check_numbers
def add_numbers(a, b):
    return a + b

@check_numbers
def multiply_numbers(x, y):
    return x * y

# Test the implementation
try:
    print(add_numbers(5, 3.5))  # Should print 8.5
    print(multiply_numbers(2, "3"))  # This should raise a ValueError
except ValueError as e:
    print("Error:", e)
