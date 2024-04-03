from functools import reduce

# Function to concatenate all strings in a given list using reduce
def concatenate_strings(string_list):
    if not string_list:
        return ""
    return reduce(lambda x, y: x + y, string_list)

# Example usage
strings = ["Hello", " ", "World", "!"]
concatenated_string = concatenate_strings(strings)
print("Concatenated string:", concatenated_string)
