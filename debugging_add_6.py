# Function to filter elements less than a threshold

def filter_low(lst, threshold=5):
    low = []
    for element in lst:
        if element < threshold:
            low.append(element)
    return low

my_list = [5, 2, 12, 7, 3, 8]
result = filter_low(my_list)
print(result)
