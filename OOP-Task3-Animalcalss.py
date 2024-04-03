class Animal:
    def speak(self):
        print("Animal can't speak")
        return self

class Dog(Animal):
    def speak(self):
        print("Woof woof")
        return self

class Cat(Animal):
    def speak(self):
        super().speak().meow()

    def meow(self):
        print("Meow meow")
        return self


# Example Usage:
dog = Dog().speak()
print("---")
cat = Cat().speak()