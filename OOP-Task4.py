# Task Nr.4:
#
# Lets say we have classes: A, B and C:
#
# Modify the program to add a method say_hello to class A that prints "Hello from class A".
# Modify the program to add a method say_hello to class B that prints "Hello from class B".
# Modify the program to add a method say_hello to class C that prints "Hello from class C".
# Create an object of class C and call the say_hello method on it. What is the output?
# Modify the program so that class B's say_hello method calls the say_hello method of class A using the super() function.
# Create an object of class C and call the say_hello method on it again. What is the output now?

class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
    def say_hello(self):
        super().say_hello()
        print("Hello from class B")

class C(B):
    def say_hello(self):
        super().say_hello()
        print("Hello from class C")

# Creating an object of class C
obj_c = C()
obj_c.say_hello()
