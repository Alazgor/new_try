# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return None

def convert_to_int(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def access_list_element(my_list, index):
    try:
        element = my_list[index]
        return element
    except IndexError as ie:
        print(f"Error: {ie}")
        return None

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        return None

def get_dictionary_value(my_dict, key):
    try:
        value = my_dict[key]
        return value
    except KeyError as ke:
        print(f"Error: {ke}")
        return None

# Example usage
print(divide_numbers(10, 0))  # Handling ZeroDivisionError
print(convert_to_int("abc"))  # Handling ValueError
print(access_list_element([1, 2, 3], 5))  # Handling IndexError
print(open_file("nonexistent_file.txt"))  # Handling FileNotFoundError
print(get_dictionary_value({"a": 1, "b": 2}, "c"))  # Handling KeyError
