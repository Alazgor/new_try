class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.address = None

    def set_name(self, name: str):
        self.name = name
        return self

    def set_age(self, age: int):
        self.age = age
        return self

    def set_address(self, address: str):
        self.address = address
        return self

    def __str__(self):
        return f"{self.name}, {self.age}, {self.address}"

person = Person()
person.set_age(25).set_name("John").set_address("123 Main St")

print(person)