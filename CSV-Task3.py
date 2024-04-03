import csv

# Read student information from the first CSV file
students_info1 = {}
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\students_info1.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        students_info1[row[0]] = row[1:]

# Read student information from the second CSV file and merge with the first
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\students_info2.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        if name in students_info1:
            students_info1[name].extend(row[1:])
        else:
            students_info1[name] = ['', ''] + row[1:]
# Write the combined information to a new CSV file
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\combined_students_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for name, info in students_info1.items():
        writer.writerow([name] + info)

print("Combined information has been saved to 'combined_students_info.csv' file.")
# Print the combined information
for name, info in students_info1.items():
    print(name, info)
