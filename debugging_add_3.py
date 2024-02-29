# This code is supposed to compare the means of two lists where the second list is an extended list of the first one.
def mean(lst):
    return sum(lst) / len(lst)

# Define the original set of values.
values = [8., 7., 9., 4., 6., 7., 8., 4.]

# Create a new list with the original values and add a few more
new_values = values[:]  # Create a copy of values using slicing
new_values.append(1.)
new_values.append(2.)
new_values.append(3.)
new_values.append(4.)
new_values.append(1.)

print(f"Difference in the mean: {mean(new_values) - mean(values)}")
