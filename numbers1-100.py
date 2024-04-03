# Using dictionary comprehensions and enumerate to find numbers divisible by 6
divisible_by_six = {index: number for index, number in enumerate(range(1, 1001)) if number % 6 == 0}

# Print the result
print(divisible_by_six)
