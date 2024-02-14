class MyString:
    def __init__(self, value: str):
        self.value = value

    def add_exclamation(self):
        self.value += "!"
        return self

    def make_upper(self):
        self.value = self.value.upper()
        return self


my_string = MyString("hello")
returned_value = my_string.add_exclamation().make_upper()

print(my_string)

print(returned_value)

print(my_string.value)