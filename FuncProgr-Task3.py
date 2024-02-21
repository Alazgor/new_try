# Write a Python program to add three given lists using Python map and lambda

# Given lists

list_1 = [1, 3, 5]
list_2 = [6, 8, 10]
list_3 = [12, 14, 16]

# Using map() with a lambda function to add corresponding elements of the lists
result = list(map(lambda x, y, z: x + y + z, list_1, list_2, list_3))

# Printing the result
print("Result:", result)
