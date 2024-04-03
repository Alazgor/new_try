# Define a lambda function to check if a string starts with a given character
starts_with_char = lambda string, char: string.startswith(char)

# Test the lambda function
input_string = input("Enter a string: ")
input_char = input("Enter a character: ")

result = starts_with_char(input_string, input_char)
print(result)

