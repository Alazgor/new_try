def addition(a: float, b: float):
    return a + b

def subtraction(a: float, b: float):
    return a - b

def multiplication(a: float, b: float):
    return a * b

def division(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError("Division is not possible: b is zero")
    return a / b

