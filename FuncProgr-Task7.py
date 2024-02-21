# Original list of numbers
original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Filtering numbers divisible by nineteen or thirteen using lambda function
divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, original_list))

# Printing the results
print("Original list:")
print(original_list)
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(divisible_by_19_or_13)
