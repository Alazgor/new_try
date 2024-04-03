class Account:

    def __init__(self, amount=0):
        self.amount = amount

    def receive_money(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"withdrawn {amount}, {self.amount} remaining")
        else:
            print("not enough money")


account1 = Account()

account2 = Account(2000)

account1.withdraw(10)

account1.receive_money(5000)

account1.withdraw(5000)

account2.withdraw(100)


class WrongGender(Exception):
    pass
class Animal:
    def __init__(self, gender):
        self.gender = gender

    def set_gender(self, gender):
        if (gender != "male") and (gender != "female"):
            raise WrongGender("it has to be either male or female")
        else:
            self.gender = gender

my_dog = Animal("male")

print(my_dog.gender)

my_dog.set_gender("female")
