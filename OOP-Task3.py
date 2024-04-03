class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded

    def give_birth(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Primate(Mammal):
    def __init__(self, name, opposable_thumbs=True, warm_blooded=True):
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs

    def swing(self):
        print(f"{self.name} is swinging from tree to tree with its opposable thumbs!")


class Chimpanzee(Primate):
    def __init__(self, name, opposable_thumbs=True, warm_blooded=True):
        super().__init__(name, opposable_thumbs, warm_blooded)

    def make_noise(self):
        print(f"{self.name} says 'Ooh ooh ahh ahh!'")

    def give_birth(self):
        print(f"{self.name} gives birth to a baby chimpanzee!")


# Test the classes
if __name__ == "__main__":
    chimp = Chimpanzee("Charlie")
    chimp.make_noise()
    chimp.give_birth()
    chimp.swing()
