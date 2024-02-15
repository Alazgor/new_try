import random

def random_number_generator(low, high, n):
    """Generator function to yield n random numbers between low and high."""
    for _ in range(n):
        yield random.randint(low, high)

# Example usage:
low = int(input("Enter the low number: "))
high = int(input("Enter the high number: "))
n = int(input("Enter the number of random numbers to generate: "))

# Generate n random numbers between low and high
random_numbers = random_number_generator(low, high, n)

# Iterate over the generator and print the random numbers
print("Random numbers generated:")
for random_number in random_numbers:
    print(random_number)
