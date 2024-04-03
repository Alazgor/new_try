def squares_generator(n):
    """Generator function to generate squares of numbers up to n."""
    for i in range(1, n + 1):
        yield i ** 2

# Example usage:
# Generate squares of numbers up to 5
squares = squares_generator(5)

# Iterate over the generator and print the squares
for square in squares:
    print(square)
