def number_generator(input_list):
    for item in input_list:
        if isinstance(item, (int, float)):
            yield item

# Example usage:
my_list = [1, 2, 'a', 3.5, 'b', 4, 5.6]
generator = number_generator(my_list)

for num in generator:
    print(num)
