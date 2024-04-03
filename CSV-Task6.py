import csv

# Read sales data from the CSV file
sales_data = {}
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\sales_data1.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the title bar
    for row in reader:
        product, quantity, price = row[1:]  # Skip the first value (date)
        quantity = int(quantity)
        price = float(price)
        revenue = quantity * price
        if product in sales_data:
            sales_data[product] += revenue
        else:
            sales_data[product] = revenue

# Write the results to a new CSV file
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\total_revenue.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Total Revenue'])
    for product, revenue in sales_data.items():
        writer.writerow([product, revenue])

print("Total revenue for each product has been calculated and saved to 'total_revenue.csv' file.")

