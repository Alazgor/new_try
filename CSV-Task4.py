import csv

# Read student information from the CSV file and handle missing values
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\students_info2.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, grade = row
        if not age:
            age = 'Unknown'
        if not grade:
            grade = 'Unknown'
        print(name, age, grade)
