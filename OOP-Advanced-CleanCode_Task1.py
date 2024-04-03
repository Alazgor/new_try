# Example 1:def greet_person(full_name):
#     """Function greets a person given full name as a string"""
#     first_name, last_name = full_name.split()
#     print(f"Hello {first_name} {last_name}, How are you today?")
#
# greet_person("John Doe")
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f"Hello, {self.name}")


person = Person("First", "Person")
person.say_hello()


# Example 2:def x(a):
#     """Function greets a person given full name as a string"""
#
#     print(f"Hello {a.split()[0]} {a.split()[1]}, How are you today?")
def greet_person(full_name):
    """Function greets a person given full name as a string"""
    first_name, last_name = full_name.split()
    print(f"Hello {first_name} {last_name}, How are you today?")

greet_person("John Doe")


# Example 3:def Greet_User (age):
#     eligiebleTo_enter = age>21
#
#     if eligiebleTo_enter == True:
#         print("Welcome")
#     if eligiebleTo_enter == False:
#         print("Access denied")
def greet_user(age):
    eligible_to_enter = age > 21

    if eligible_to_enter:
        print("Welcome")
    else:
        print("Access denied")


greet_user(25)
