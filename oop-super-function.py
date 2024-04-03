class Parent:
    def greet(self):
        print("Hello from Parent class")


class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello fron Child class")

child = Child()

child.greet()
