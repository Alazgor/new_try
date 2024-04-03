# Given list of integers
numbers = [15, 30, 45, 60, 70]

# Using lambda functions with map to square and cube every number
square_cube = list(map(lambda x: (x ** 2, x ** 3), numbers))
print(square_cube)


