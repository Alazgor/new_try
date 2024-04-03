try:
    my_list = [1, 2, 3, 4, 5]
    index_to_access = 10
    value = my_list[index_to_access]
    print("Value at index", index_to_access, ":", value)
except IndexError as ie:
    print(f"IndexError: {ie}")
    print("The index is out of bounds. Please choose a valid index.")
