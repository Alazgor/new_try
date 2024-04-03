import csv

# Define the URL or file path of the CSV file
file_path = "C:\\Users\\aleks\\CodeAcademy\\pythonProject\\sales_data.csv"

# Open the CSV file and read its content
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)

    # Print header
    print("Date\tProduct\tQuantity\tPrice")

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Convert quantity to an integer
        quantity = int(row['Quantity'])

        # Check if the quantity sold is greater than 10
        if quantity > 10:
            # Print the row if the condition is met
            print(f"{row['Date']}\t{row['Product']}\t{row['Quantity']}\t{row['Price']}")
