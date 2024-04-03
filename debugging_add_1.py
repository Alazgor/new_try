# This code is supposed to compute an average of a list of numbers


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

numbers = [5, 10, 15, 20]
result = calculate_average(numbers)
print(result)
