# class Animal:
#     def __init__(self, name, number_of_legs=4):
#         self.name = name
#         self.number_of_legs = number_of_legs
#
#     def make_sound(self):
#         print("some sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, 4)
#         self.breed = breed
#
#     def make_sound(self):
#         print("Bark")
#
#
# class Cat(Animal):
#     def __init__(self, name, fur_color):
#         super().__init__(name, 4)
#         self.fur_color = fur_color
#
#     def make_sound(self):
#         print("Meow")
#
# class DogCat(Dog, Cat):
#     def __init__(self, name, breed, fur_color):
#         Dog.__init__(self, name, breed)
#         Cat.__init__(self, name, fur_color)
#
# dogcat = DogCat(name="DogKitty", breed = "Mixed", fur_color="Black")
# print(dogcat.name)
# print(dogcat.breed)
# print(dogcat.fur_color)
# dogcat.make_sound()

class Animal:
    def __init__(self, name, number_of_legs=4):
        self.name = name
        self.number_of_legs = number_of_legs

    def make_sound(self):
        print("some sound")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 4)
        self.breed = breed

    def make_sound(self):
        print("Meow")


class WildCat(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name, 4)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar")

    def hunt(self):
        print("hunted a rabbit")


class Tiger(WildCat, Cat):
    def __init__(self, name, breed, fur_color):
        super().__init__(name, breed)
        Cat.__init__(self, name, fur_color)


tiger = Tiger(name="Tiger King", breed="wild", fur_color="striped")
print(tiger.name)
print(tiger.breed)
print(tiger.fur_color)
tiger.make_sound()