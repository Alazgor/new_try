# 4. Write a decorator that "slows down functions" before calling a function. This can be useful if many users are trying to
# connect to your server and you don('t want a single user to overload your server. '
# 'Wasting time can be achieved with time.sleep(1))

import time
from functools import wraps

def slow_down(func):
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)  # Slow down the function by 1 second
        return func(*args, **kwargs)
    return wrapper_slow_down

# Example usage:
@slow_down
def my_function():
    print("This function is slowed down by 1 second.")

# Call the function
my_function()
