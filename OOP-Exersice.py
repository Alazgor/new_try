

# Create a few examples of yourself where you show four pillars of OOP in action.
class Tree:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def grow(self):
        self.__age += 1

# Inheritance: FruitTree inherits from Tree
class FruitTree(Tree):
    def __init__(self, name, age, fruit):
        super().__init__(name, age)
        self.fruit = fruit

    def produce_fruit(self):
        return f"{self.get_name()} produced {self.fruit}."

# Polymorphism: PineTree is treated as a 'Tree'
class PineTree(Tree):
    def __init__(self, name, age, needle_length):
        super().__init__(name, age)
        self.needle_length = needle_length

    def display_info(self):
        return f"{self.get_name()} is a pine tree with needle length {self.needle_length}."

# Example usage
oak_tree = Tree("Oak", 10)
apple_tree = FruitTree("Apple", 5, "apples")
pine_tree = PineTree("Pine", 8, "long")

# Polymorphism: Different types of trees treated as 'Tree'
trees = [oak_tree, apple_tree, pine_tree]
for tree in trees:
    # Check if the tree has a 'display_info' method before calling it
    if hasattr(tree, 'display_info'):
        print(tree.display_info())
    else:
        print(f"{tree.get_name()} is {tree.get_age()} years old.")
