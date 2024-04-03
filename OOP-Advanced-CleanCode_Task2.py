def is_magic_number(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number == 1

# Test cases
print(is_magic_number(50113))
print(is_magic_number(1234))
print(is_magic_number(123))
