from functools import reduce

# Task 1: Find the maximum value within a given list of integers using reduce
def find_max_value_with_reduce(integer_list):
    if not integer_list:
        return None
    return reduce(lambda x, y: x if x > y else y, integer_list)

# Example usage for Task 1
numbers = [3, 7, 2, 9, 5]
max_value = find_max_value_with_reduce(numbers)
print("Maximum value in the list:", max_value)