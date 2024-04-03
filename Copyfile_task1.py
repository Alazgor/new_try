import os
import re
from datetime import datetime

# Function to add date and time to the last line of the file
def add_date_time(file_name):
    with open(file_name, 'a') as file:
        file.write("\nDate and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Function to replace the first occurrence of a phrase in the file
def replace_first_occurrence(file_name, old_text, new_text):
    with open(file_name, 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write(content.replace(old_text, new_text, 1))

# Function to print the text of the file in reverse order
def print_reverse(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        print(text[::-1])

# Function to count words, numbers, uppercase, and lowercase letters in the text of the file
def count_chars(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = len(re.findall(r'\b\w+\b', text))
        numbers = len(re.findall(r'\d+', text))
        uppercase = sum(1 for char in text if char.isupper())
        lowercase = sum(1 for char in text if char.islower())
        print(f"Words: {words}\nNumbers: {numbers}\nUppercase: {uppercase}\nLowercase: {lowercase}")

# Function to copy the text of the file to a new file, converting it to uppercase letters only
def copy_to_uppercase(file_name, new_file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    with open(new_file_name, 'w') as new_file:
        new_file.write(text.upper())

# Creating the original file with the text from "import this"
with open("Text.txt", 'w') as file:
    import this
    add_date_time("Text.txt")

# Printing the text from the created file
print("Text from created file:")
with open("Text.txt", 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

# Adding today's date and time to the last line
add_date_time("Text.txt")

# Adding line numbers
with open("Text.txt", 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for i, line in enumerate(lines, start=1):
        file.write(f"{i}. {line}")

# Replacing the line "Beautiful is better than ugly."
replace_first_occurrence("Text.txt", "Gražu yra geriau nei negražu", "Beautiful is better than ugly.")

# Printing the text of the file in reverse order
print("\nText from created file in reverse:")
print_reverse("Text.txt")

# Printing the number of words, numbers, uppercase, and lowercase letters
print("\nCounts:")
count_chars("Text.txt")

# Copying the text of the file to a new file, converting it to uppercase letters only
copy_to_uppercase("Text.txt", "Uppercase_Text.txt")

