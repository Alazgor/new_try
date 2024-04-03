text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# Create an empty dictionary to store letter occurrences
letter_occurrences = {}

# Loop through each character in the text
for char in text:
    # Check if the character is a letter
    if 'a' <= char.lower() <= 'z':
        # Convert the letter to lowercase for case-insensitivity
        char = char.lower()
        # Update the count in the dictionary
        letter_occurrences[char] = letter_occurrences.get(char, 0) + 1

# Print the result
print("Letter occurrences:")
for letter, count in letter_occurrences.items():
    print(f"{letter}: {count}")

