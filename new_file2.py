import random

class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        self.tank_loc_x = 4
        self.tank_loc_y = 6
        self.tank_direction = "up"  # Default direction is "up"
        self.total_shots = 0
        self.hits = 0  # New variable to track hits
        self.shots = []
        self.target_move_countdown = 1  # Countdown for target movement
        self.generate_new_targets()

    def generate_new_targets(self):
        """Generate new random locations for the targets."""
        # Generate the first target location
        self.target1_loc_x, self.target1_loc_y = self.tank_loc_x, self.tank_loc_y
        while (self.target1_loc_x, self.target1_loc_y) == (self.tank_loc_x, self.tank_loc_y):
            self.target1_loc_x = random.randint(1, self.N - 2)
            self.target1_loc_y = random.randint(1, self.N - 2)

        # Generate the second target location
        self.target2_loc_x, self.target2_loc_y = self.tank_loc_x, self.tank_loc_y
        while (
            (self.target2_loc_x, self.target2_loc_y) == (self.tank_loc_x, self.tank_loc_y)
            or (self.target2_loc_x, self.target2_loc_y) == (self.target1_loc_x, self.target1_loc_y)
        ):
            self.target2_loc_x = random.randint(1, self.N - 2)
            self.target2_loc_y = random.randint(1, self.N - 2)

    def print_map(self):
        """Print the current map of the game."""
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                elif (j, i) == (self.target1_loc_x, self.target1_loc_y):
                    print(" E ", end="")
                elif (j, i) == (self.target2_loc_x, self.target2_loc_y):
                    print(" Y ", end="")
                elif any((j, i) == (x, y) for x, y, _ in self.shots):
                    print(" * ", end="")
                else:
                    print(" . ", end="")
            print()

    def move_targets(self):
        """Move the targets every player move."""
        if self.target_move_countdown == 0:
            move_options = ["up", "down", "left", "right"]

            # Move the first target
            new_x, new_y = self.target1_loc_x, self.target1_loc_y
            while (new_x, new_y) == (self.target1_loc_x, self.target1_loc_y):
                direction = random.choice(move_options)
                new_x, new_y = self.move_in_direction(self.target1_loc_x, self.target1_loc_y, direction)

            self.target1_loc_x, self.target1_loc_y = new_x, new_y

            # Move the second target
            new_x, new_y = self.target2_loc_x, self.target2_loc_y
            while (
                (new_x, new_y) == (self.target2_loc_x, self.target2_loc_y)
                or (new_x, new_y) == (self.target1_loc_x, self.target1_loc_y)
            ):
                direction = random.choice(move_options)
                new_x, new_y = self.move_in_direction(self.target2_loc_x, self.target2_loc_y, direction)

            self.target2_loc_x, self.target2_loc_y = new_x, new_y

            self.target_move_countdown = 1  # Reset the countdown
        else:
            self.target_move_countdown -= 1

    def move_in_direction(self, x, y, direction):
        """Move in the specified direction."""
        if direction == "up" and y > 0:
            return x, y - 1
        elif direction == "down" and y < self.N - 1:
            return x, y + 1
        elif direction == "left" and x > 0:
            return x - 1, y
        elif direction == "right" and x < self.N - 1:
            return x + 1, y
        return x, y

    def check_hit(self, x, y):
        """Check if the coordinates (x, y) hit any of the targets."""
        hit_target1 = (x, y) == (self.target1_loc_x, self.target1_loc_y)
        hit_target2 = (x, y) == (self.target2_loc_x, self.target2_loc_y)

        if hit_target1 or hit_target2:
            self.hits += 1  # Increment hits count
            self.generate_new_targets()  # Generate new targets after hitting
            self.target_move_countdown = 1  # Reset the countdown

        return hit_target1 or hit_target2

    def fire(self):
        """Fire a shot."""
        tank_direction = self.tank_direction
        shot_x, shot_y = self.tank_loc_x, self.tank_loc_y

        self.shots.append((shot_x, shot_y, tank_direction))
        self.total_shots += 1

        # Check if the shot hits any of the targets
        if self.check_hit(shot_x, shot_y):
            print("Target hit!")

    def get_tank_direction(self):
        """Get the tank's current direction."""
        return self.tank_direction

    def left(self):
        """Move the tank left."""
        if self.tank_loc_x > 0:
            self.tank_loc_x -= 1
            self.tank_direction = "left"

    def right(self):
        """Move the tank right."""
        if self.tank_loc_x < self.N - 1:
            self.tank_loc_x += 1
            self.tank_direction = "right"

    def forward(self):
        """Move the tank forward."""
        if self.tank_loc_y > 0:
            self.tank_loc_y -= 1
            self.tank_direction = "up"

    def back(self):
        """Move the tank backward."""
        if self.tank_loc_y < self.N - 1:
            self.tank_loc_y += 1
            self.tank_direction = "down"

    def move_shots(self):
        """Move the shots independently."""
        new_shots = []
        for x, y, direction in self.shots:
            new_x, new_y = self.move_in_direction(x, y, direction)
            new_shots.append((new_x, new_y, direction))

        self.shots = new_shots

    def info(self):
        """Display information about the tank."""
        print(f"Tank Direction: {self.get_tank_direction()}")
        print(f"Tank Coordinates: ({self.tank_loc_x}, {self.tank_loc_y})")
        print(f"Total Shots: {self.total_shots}")
        print(f"Total Hits: {self.hits}")  # Display hits count
        print(f"Shots in Each Direction: {self.shots}")
        print(f"Target 1 Coordinates: ({self.target1_loc_x}, {self.target1_loc_y})")
        print(f"Target 2 Coordinates: ({self.target2_loc_x}, {self.target2_loc_y})")

if __name__ == "__main__":
    tg = TankGame()

    while True:
        tg.print_map()
        command = input("Input a command (left/l, right/r, forward/f, back/b, A/fire, info/i, quit/q): ")

        if command.lower() in ['left', 'l']:
            tg.left()
        elif command.lower() in ['right', 'r']:
            tg.right()
        elif command.lower() in ['forward', 'f']:
            tg.forward()
        elif command.lower() in ['back', 'b']:
            tg.back()
        elif command.lower() in ['fire', 'a']:
            tg.fire()

        tg.move_targets()  # Move the targets after each command
        tg.move_shots()  # Move the shots independently after each command

        if command.lower() in ['info', 'i']:
            tg.info()
        elif command.lower() in ['quit', 'q']:
            break
        else:
            print("Invalid command. Please enter 'left', 'right', 'forward', 'back', 'A', 'quit'.")
