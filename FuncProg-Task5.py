# Define a lambda function for converting integers to strings
int_to_str = lambda num: str(num)


def convert_to_strings(int_list, int_tuple):
    # Convert list of integers to list of strings using lambda function
    string_list = list(map(int_to_str, int_list))

    # Convert tuple of integers to list of strings using lambda function
    string_tuple = list(map(int_to_str, int_tuple))

    return string_list, string_tuple


# Example usage
if __name__ == "__main__":
    # Given list of integers
    int_list = [1, 2, 3, 4, 5]

    # Given tuple of integers
    int_tuple = (6, 7, 8, 9, 10)

    # Convert to strings
    string_list, string_tuple = convert_to_strings(int_list, int_tuple)

    # Print the result
    print("List of integers converted to strings:", string_list)
    print("Tuple of integers converted to strings:", string_tuple)
