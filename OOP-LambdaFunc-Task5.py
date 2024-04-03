# Original list of tuples
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list of tuples based on the second element of each tuple
sorted_list = sorted(original_list, key=lambda x: x[1])

# Printing the sorted list of tuples
print("Sorted the List of Tuples:")
print(sorted_list)
