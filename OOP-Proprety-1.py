class Person:
    def __init__(self, name, age, friends):
        # Property setting (using data validation potentially!)
        self.name = name
        self.age = age
        self.friends = friends

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a: int):
        # Data validation
        if 0 <= a <= 150:
            self._age = a
        else:
            raise ValueError("Age is not valid!")

    def del_age(self):
        self._age = None

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend_list: list):
        # Data validation
        for friend in friend_list:
            if not isinstance(friend, str):
                raise ValueError(f"{friend} is not string!")
            if len(friend) == 0:
                raise ValueError("There is a friend with no name!")
        self._friends = friend_list.copy()

    def del_friends(self):
        self._friends = []


pers1 = Person("Paulius", 12, ["john", "mary"])
pers2 = Person("John", 22, ["paulius"])
# pers1.age = -2
print(pers1.name, pers1.age, pers1.friends)
pers1.del_age()
pers1.del_friends()
print(pers1.name, pers1.age, pers1.friends)
