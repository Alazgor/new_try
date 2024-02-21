result = (lambda numb1, numb2: numb1 * numb2)(
    numb1=(lambda numb: numb + 15)(numb=0),
    numb2=(lambda numb: numb + 15)(numb=0)
)

print(result)

# Lambda function to add 15 to a given number
add_15 = lambda x: x + 15

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Example usage of the lambda functions
number = 10
print("Adding 15 to", number, ":", add_15(number))

x = 5
y = 6
print("Multiplying", x, "and", y, ":", multiply(x, y))
