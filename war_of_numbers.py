def war_of_numbers(numbers):
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return abs(sum_even - sum_odd)

# Test cases
print(war_of_numbers([2, 8, 7, 5]))  # Output: 2
print(war_of_numbers([12, 90, 75]))  # Output: 27
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))  # Output: 168
