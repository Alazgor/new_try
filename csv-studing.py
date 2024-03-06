import requests
import csv

# URL of the CSV file
url = "https://raw.githubusercontent.com/karina-klinkeviciute/PTUAE1/main/csv_sales_data.csv"

# Load the file
response = requests.get(url)

# Check if the download was successful
if response.status_code == 200:
    # Read the content of the CSV file
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content)

    # Display the content of the CSV file
    for row in csv_reader:
        print(row)
else:
    print("Failed to download the file")

