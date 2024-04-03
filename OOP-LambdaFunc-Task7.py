# Original Matrix 1
original_matrix_1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# Sort the matrix 1 in ascending order according to the sum of its rows
sorted_matrix_1 = sorted(original_matrix_1, key=lambda row: sum(row))

# Printing the sorted matrix 1
print("Original Matrix 1:", original_matrix_1)
print("Sorted Matrix 1:", sorted_matrix_1)

# Original Matrix 2
original_matrix_2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Sort the matrix 2 in ascending order according to the sum of its rows
sorted_matrix_2 = sorted(original_matrix_2, key=lambda row: sum(row))

# Printing the sorted matrix 2
print("Original Matrix 2:", original_matrix_2)
print("Sorted Matrix 2:", sorted_matrix_2)
