# 1. Write a decorator with an argument runs which is the number of times to call the function and which prints the average
# time the decorated function took over the runs times. For example the decorated long_function() should output
# “This function took an average of 1.23 seconds to run, averaged over 5 runs”
import time
import functools

def average_time(runs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(runs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)
            average_time = total_time / runs
            print(f"This function took in average {average_time:.2f} seconds, averaged over {runs} runs")
            return result
        return wrapper
    return decorator

# Example usage
@average_time(runs=5)
def long_function():
    time.sleep(1.23)  # Simulating a long-running function

long_function()

