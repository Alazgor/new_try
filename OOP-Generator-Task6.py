# List of tuples containing person's information: (name: str, age: int, city: str, salary: float)
people_info = [
    ("Alice", 25, "New York", 50000.0),
    ("Bob", 30, "Los Angeles", 60000.0),
    ("Charlie", 35, "Chicago", 70000.0),
    ("David", 40, "Houston", 80000.0),
    ("Eve", 45, "Philadelphia", 90000.0)
]

# Filtering Generator: Filters people who are below a certain age threshold
def filter_below_age(people, threshold):
    for person in people:
        if person[1] < threshold:
            yield person

# Mapping Generator: Maps the names of people to uppercase
def map_to_upper(people):
    for person in people:
        yield (person[0].upper(),) + person[1:]

# Aggregation Generator: Calculates the average salary of the selected group
def calculate_average_salary(people):
    total_salary = 0
    count = 0
    for person in people:
        total_salary += person[3]
        count += 1
    if count > 0:
        yield total_salary / count
    else:
        yield 0

# Example usage:
filtered_generator = filter_below_age(people_info, 35)
uppercased_generator = map_to_upper(filtered_generator)
average_salary_generator = calculate_average_salary(uppercased_generator)

# Printing the results
print("People below 35 years old:")
for person in filtered_generator:
    print(person)

print("\nNames mapped to uppercase:")
for person in uppercased_generator:
    print(person)

print("\nAverage salary of the selected group:")
for avg_salary in average_salary_generator:
    print(avg_salary)
