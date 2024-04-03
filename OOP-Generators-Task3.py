# Write a Python program to create a generator that iterates over a string.
def string_iterator(string):
    """Generator function to iterate over a string."""
    for char in string:
        yield char

# Example usage:
input_string = input("Enter a string: ")

# Iterate over the generator and print each character of the string
print("Characters in the string:")
for char in string_iterator(input_string):
    print(char)
