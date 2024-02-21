# Original array of integers
original_array = [1, 2, 3, 5, 7, 8, 9, 10]

# Counting even numbers using lambda function
even_count = len(list(filter(lambda x: x % 2 == 0, original_array)))

# Counting odd numbers using lambda function
odd_count = len(list(filter(lambda x: x % 2 != 0, original_array)))

# Printing the results
print("Original array:")
print(original_array)
print("\nNumber of even numbers in the above array:", even_count)
print("Number of odd numbers in the above array:", odd_count)


from functools import reduce

# Original array of integers
original_array = [1, 2, 3, 5, 7, 8, 9, 10]

# Function to count even numbers
count_even = reduce(lambda count, num: count + 1 if num % 2 == 0 else count, original_array, 0)

# Function to count odd numbers
count_odd = reduce(lambda count, num: count + 1 if num % 2 != 0 else count, original_array, 0)

# Printing the results
print("Original array:")
print(original_array)
print("\nNumber of even numbers in the above array:", count_even)
print("Number of odd numbers in the above array:", count_odd)
