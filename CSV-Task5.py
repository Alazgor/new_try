import csv

# Read student information from the CSV file and validate each row
with open('C:\\Users\\aleks\\CodeAcademy\\pythonProject\\students_info3.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, grade = row
        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be a positive integer")
            if grade not in ['A', 'B', 'C', 'D', 'F']:
                raise ValueError("Invalid grade")
            print(name, age, grade)
        except ValueError as e:
            print("Validation failed for row:", row, "-", e)
