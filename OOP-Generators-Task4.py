def fibonacci_generator():
    """Generator function to generate Fibonacci series."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fibonacci_series = fibonacci_generator()

# Generate and print the first 10 Fibonacci numbers
print("Fibonacci series:")
for _ in range(10):
    print(next(fibonacci_series))
