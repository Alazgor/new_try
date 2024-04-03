# Initialize variables for sum and count
sum_of_numbers = 0
count_of_numbers = 0

# Use a loop to get 10 integers from the user
for i in range(10):
    try:
        # Get input from the user and convert it to an integer
        number = int(input(f"Enter integer #{i + 1}: "))

        # Add the entered number to the sum
        sum_of_numbers += number

        # Increment the count of entered numbers
        count_of_numbers += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate the average
average_of_numbers = sum_of_numbers / count_of_numbers if count_of_numbers > 0 else 0

# Print the sum and average
print(f"Sum of entered numbers: {sum_of_numbers}")
print(f"Average of entered numbers: {average_of_numbers}")
