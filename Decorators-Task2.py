# 2. Write a decorator that allows you to pass only string parameters to a function.

def only_strings(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("Function '{}' only accepts string parameters.".format(func.__name__))
        for kwarg in kwargs.values():
            if not isinstance(kwarg, str):
                raise ValueError("Function '{}' only accepts string parameters.".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

# Example usage:
@only_strings
def print_strings(*strings):
    for string in strings:
        print(string)

print_strings("Hello", "World")  # Output: Hello\nWorld
try:
    print_strings("Hello", 42)  # This should raise a ValueError
except ValueError as e:
    print("Error:", e)
