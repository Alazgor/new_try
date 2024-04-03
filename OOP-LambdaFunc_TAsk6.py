# Original list of dictionaries
original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the list of dictionaries based on the 'color' value
sorted_list = sorted(original_list, key=lambda x: x['color'])

# Printing the sorted list of dictionaries
print("Sorted the List of dictionaries:")
print(sorted_list)
