class Car:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.direction = "north"

    def turn_left(self):
        if self.direction == "north":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "north"
        return self

    def turn_right(self):
        if self.direction == "north":
            self.direction = "east"
        elif self.direction == "west":
            self.direction = "north"
        elif self.direction == "south":
            self.direction = "west"
        elif self.direction == "east":
            self.direction = "south"
        return self

    def go(self, distance):
        if self.direction == "north":
            self.position_y += distance
        if self.direction == "south":
            self.position_y -= distance
        if self.direction == "west":
            self.position_x -= distance
        if self.direction == "east":
            self.position_x += distance
        return self

    def show_position(self):
        print(f"I am at {self.position_x} : {self.position_y}")
        return self

car = Car().turn_left().go(50).turn_left().go(20).show_position().go(40).turn_right().go(80).show_position().go(50).turn_right()
