class LengthError(Exception):
    pass

def enter_code():
    code = input("Enter a two-letter code:")

    if len(code) != 2:
        raise LengthError("It is not two letters")
    else:
        return code

try:
    our_code = enter_code()
    print(our_code)
except LengthError as exc:
    print(exc.args)

