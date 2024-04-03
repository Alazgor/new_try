# Write a Python program to add two given lists and find the difference between lists. Use map() function.

def add_lists(list1, list2):
    # Add corresponding elements of two lists
    sum_list = list(map(lambda x, y: x + y, list1, list2))
    return sum_list

def find_difference(list1, list2):
    # Find the difference between corresponding elements of two lists
    diff_list = list(map(lambda x, y: x - y, list1, list2))
    return diff_list

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Add two lists
sum_result = add_lists(list1, list2)
print("Sum of the lists:", sum_result)

# Find the difference between two lists
diff_result = find_difference(list1, list2)
print("Difference between the lists:", diff_result)
