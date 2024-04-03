from functools import reduce

# Given list of integers
integer_list = [1, 2, 3, 4, 5]

# Using reduce to multiply all values
product = reduce(lambda x, y: x * y, integer_list)

# Printing the result
print("The product of all values in the list:", product)
