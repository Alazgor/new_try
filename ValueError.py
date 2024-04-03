def get_user_input():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)  # Try converting input to a float
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program
try:
    user_number = get_user_input()
    print("You entered:", user_number)
except ValueError as ve:
    print(f"Error: {ve}")