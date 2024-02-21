class AgeTooLow(Exception):
    def __init__(self, age):
        self.message = f"User should be at least 21 years old! Current user is {age} years old."
        super().__init__(self.message)

class AgeTooHigh(Exception):
    def __init__(self, age):
        self.message = f"User is too old for this gambling website! Current user is {age} years old."
        super().__init__(self.message)

users_age = int(input("Enter your age: "))

if users_age < 21:
   raise AgeTooLow(users_age)
elif users_age > 100:
   raise AgeTooHigh(users_age)
else:
   print("Welcome to the gambling website!")
