def puzzle_pieces(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        return False

    # Calculate the sums of corresponding elements
    sums = [a + b for a, b in zip(list1, list2)]

    # Check if all sums are equal
    return all(x == sums[0] for x in sums)

# Test cases
print(puzzle_pieces([3, 6], [9, 6]))
print(puzzle_pieces([-2, 0, ], [2, 0, ]))
print(puzzle_pieces([1, 3, 5], [2, 4, 6]))
print(puzzle_pieces([9, 6, 3], [3, 6, 9]))

