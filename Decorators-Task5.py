# 5. Write a decorator with an argument runs which is the number of times to call the function and which prints
# the average time the decorated function took over the runs times. For example long_function() should output
# "This function took an average of 1.23 seconds to run, averaged over 5 runs"
def debug(func):
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f"{k}={repr(v)}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(result)}")
        return result
    return wrapper

# Example usage:
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

# Test the implementation
print(make_greeting("Benjamin"))

