# Get user input for a number
user_input = int(input("Enter a number: "))

# Check if the square root of the number is an integer
square_root = int(user_input**0.5)

# Print the result
if square_root**2 == user_input:
    print(f"{user_input} is a perfect square.")
else:
    print(f"{user_input} is not a perfect square.")