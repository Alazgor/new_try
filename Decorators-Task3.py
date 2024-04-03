# 3. Write a python decorator that would return whether the result of a function is even or uneven. Make sure it works
# for arbitrary inputs. For example, if you decorate the following function with this decorator: sum_two_numbers(1, 2)we
# will get (3, 'odd')
def even_or_odd(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            if result % 2 == 0:
                result_type = 'even'
            else:
                result_type = 'odd'
            return result, result_type
        else:
            raise ValueError("Result is not an integer.")
    return wrapper

@even_or_odd
def sum_two_numbers(a, b):
    return a + b

# Example usage:
result, result_type = sum_two_numbers(1, 2)
print(f"The result is {result} and it's {result_type}.")  # Output: The result is 3 and it's odd.


