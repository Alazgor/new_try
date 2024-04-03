# Using list comprehension to find numbers containing the digit 9
numbers_with_nine = [number for number in range(1, 1001) if '9' in str(number)]

# Print the result
print(numbers_with_nine)
