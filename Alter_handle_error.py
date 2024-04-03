from typing import Union

def My_dummy_int_func(a: Union[str, float]) -> None:
    try:
        int_value = int(a)
        print(int_value)
    except ValueError:
        print(f"Value of '{a}' cannot be deduced as an integer.")
    except TypeError:
        print(f'Type of value "{a}" is incompatible.')

My_dummy_int_func(1)

