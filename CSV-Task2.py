import csv

# Define the path to the CSV file
file_path = "C:\\Users\\aleks\\CodeAcademy\\pythonProject\\employees.csv"

# Read data from the CSV file
employees = []
with open(file_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)

# Increase the salary of each employee by 10%
for employee in employees:
    employee['Salary'] = str(float(employee['Salary']) * 1.1)

# Write the updated data back to the same CSV file
with open(file_path, mode='w', newline='') as file:
    fieldnames = ['Name', 'Salary']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for employee in employees:
        writer.writerow(employee)

print("Employee salaries have been successfully increased by 10% and written back to the file.")
