# Function to remove even numbers from a list
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_even_numbers(numbers)
print(result)

# Iterate over the list backwards to avoid index shifting when removing elements
# for i in range(len(my_list) - 1, -1, -1):
#     if my_list[i] % 2 != 0:
#         del my_list[i]
# print(my_list)