class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        if self._is_age_verified(age):
            self._age = age
        else:
            raise ValueError("Age is not an integer or 0 <= x <= 150")

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_age(self) -> int:
        return self._age

    def _is_age_verified(self, age: int) -> bool:
        # Perform reasonable checks for age
        if not isinstance(age, int):
            print("Age is not an integer!")
            return False
        if age < 0:
            print("Age cannot be negative!")
            return False
        if age > 150:
            print("People cannot get older than 150 years!")
            return False
        return True

    def set_age(self, age: int):
        if self._is_age_verified(age):
            self._age = age

# Testing the class
pers1 = Person("Alice", 12)
print(pers1.get_name())
print(pers1.get_age())
pers1.set_age(24)
print(pers1.get_age())

pers2 = Person("Bob", 33)
print(pers2.get_name())
print(pers2.get_age())
