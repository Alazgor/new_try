# The following should return True if the input is 1 or 2


def is_1_or_2(num):
    if num == 1 or num == 2:
        print('the number is 1 or 2')
        return True
    else:
        print('the number is not 1 or 2')
        return False

result = is_1_or_2(2)
print(result)
