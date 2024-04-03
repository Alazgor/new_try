# Taking a list and would return a new list at only at first and last elements

def list_of_first_and_last(input_list):
    return [input_list[0], input_list[-1]]

print(list_of_first_and_last([1, 2, 3]))
print(list_of_first_and_last(["banana", "orange", "grape", "pinapple", "tomate"]))

var_list = [1, 2, 3, 7, 9, 11, 2, 1, 7]
print(list_of_first_and_last(var_list))

