# Write a Python program to triple all numbers of a given list of integers. Use Python map().

# Given list of integers
numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda function to triple all numbers
tripled_numbers = list(map(lambda x: x * 3, numbers))

# Printing the tripled numbers
print("Original list:", numbers)
print("Tripled numbers:", tripled_numbers)
