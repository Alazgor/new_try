# Generate a dictionary of 10 keys (1,2,3...10).
# Each of them should store a value of random integer number from 1 to 100.

import random

my_dictionary = {}

for key in range(1, 11):
    value = random.randint(1, 100)
    my_dictionary[key] = value

print(my_dictionary)