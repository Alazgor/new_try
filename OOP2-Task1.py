from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def get_name(self):
        return self.name


class Dog(Animal):
    def speak(self):
        return "Dog says Woof!"


class Cat(Animal):
    def speak(self):
        return "Cat says Meow!"


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.get_name(), dog.speak())
print(cat.get_name(), cat.speak())
