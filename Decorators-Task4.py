# 4. write a debug decorator that would help you debug function calls. For example, it should print out the way the
# function was called, specifically: take the repr(a) of any positional argument to the function,
# all{k}={repr(v)} keyword-value pairs from keyword arguments. Print out the function name and finally which value
# the function returned. For example, if I have
# @debug
# def make_greeting(name, age=None):
#      if age is None:
#          return f"Howdy {name}!"
#      else:
#          return f"Whoa {name}! {age} already, you're growing up!"
# and then I expect the following output
# >>> make_greeting("Benjamin")
# Calling make_greeting('Benjamin')
# make_greeting() returned 'Howdy Benjamin!'
# 'Howdy Benjamin!'

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
print(make_greeting(name="Benjamin", age="36"))
