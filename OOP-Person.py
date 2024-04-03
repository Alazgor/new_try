class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


person = Person("Jonas", 42, "Laisves al. 45, Kaunas")

print(person.name)

person2 = Person("Petras", 21, "Savanoriu 11, Kaunas")

print(person2.age)

person2.age = 27

print(person2.age)

class House:
    city: str = "Kaunas"

    def __init__(self, cost, age, owner):
        self.cost = cost
        self.age = age
        self.owner = owner

    def get_cost(self):
        return f"cost of this house is {self.cost}"

    def sell(self, buyer):
        self.owner = buyer

    def set_colour(self, colour="white"):
        self.colour = colour

    def get_colour(self):
        if hasattr(self, "colour"):
            return f"the colour of the house is {self.colour}"
        else:
            return "blue"
# print(House)

house1 = House(120000, 12, "Jonas")

house2 = House(205000, 5, "Petras")

print(house1.cost)

print(house1.city)

print(house2.city)

print(house1.get_cost())

print(house2.get_cost())

house2.sell("Agne")

print(house2.owner)

house2.colour = "yellow-blue"

print(house2.colour)

print(house1.get_colour())

