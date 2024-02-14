from dataclass import dataclass

# class Person:
    # def __init__(self, name, age, email):
    #     self.name = name
    #     self.age = age
    #     self.email = email
    self.adress = ""

@dataclass
class Person:
    name: str
    age: int
    email: str
    adress: str = ""

person = Person("John", 25, "john@example.com")

print(person)

@dataclass
class Point:
    x: float
    y: float


    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    point = Point(3, 4)
    print(point.distance_from_origin())  # Output: 5.0