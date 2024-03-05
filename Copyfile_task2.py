# Function to get input from the user until an empty line is entered
def get_input():
    lines = []
    while True:
        line = input("Enter a line (press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

# Function to write the entered lines to a file
def write_to_file(lines, file_name):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Allowing the user to enter the desired number of lines
num_lines = int(input("Enter the number of lines: "))

# Allowing the user to enter the desired name of the file
file_name = input("Enter the name of the file to be created: ")

# Getting input from the user until an empty line is entered
lines = get_input()

# Writing the entered text as separate lines to a file
write_to_file(lines, file_name)

print(f"File '{file_name}' has been created with {len(lines)} lines.")
