# 1. Write a decorator that limits the number of parameters (say no more than 2 parameters for a function)

@debug
def make_greeting(name, age=None):
     if age is None:
         return f"Howdy {name}!"
     else:
         return f"Whoa {name}! {age} already, you're growing up!"
and then I expect the following output
>>> make_greeting("Benjamin")
Calling make_greeting('Benjamin')
make_greeting() returned 'Howdy Benjamin!'
'Howdy Benjamin!'


def max_parameters(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) + len(kwargs) > limit:
                raise ValueError(f"Function '{func.__name__}' accepts at most {limit} parameters.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
@max_parameters(2)
def example_function(a, b):
    return a + b

print(example_function(1, 2))  # Output: 3
try:
    print(example_function(1, 2, 3))  # This should raise a ValueError
except ValueError as e:
    print("Error:", e)
