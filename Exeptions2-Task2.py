class CalculatorInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise CalculatorInputError(f"Invalid expression: {e}")

while True:
    user_input = input("Enter an expression (e.g., '1 + 5'): ")
    if user_input.lower() == 'quit':
        break
    try:
        result = calculate(user_input)
        print("Result:", result)
    except CalculatorInputError as e:
        print(e.message)
    except Exception as e:
        print("An unexpected error occurred")








