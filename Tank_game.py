import random

class TankGame:
    def __init__(self, N: int = 7, initial_points: int = 100, max_shots_displayed: int = 3):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        :param initial_points: initial points for the player.
        :param max_shots_displayed: maximum number of shots to display on the field.
        """
        self.N = N
        self.tank_loc_x = 4
        self.tank_loc_y = 6
        self.tank_direction = "up"
        self.total_shots = 0
        self.hits = 0
        self.points = initial_points
        self.shots = []
        self.max_shots_displayed = max_shots_displayed
        self.target_move_countdown = 1
        self.generate_new_target()
        self.top_players = []

    def generate_new_target(self):
        """Generate a new random location for the target."""
        self.target_loc_x, self.target_loc_y = self.tank_loc_x, self.tank_loc_y
        while (self.target_loc_x, self.target_loc_y) == (self.tank_loc_x, self.tank_loc_y):
            self.target_loc_x = random.randint(1, self.N - 2)
            self.target_loc_y = random.randint(1, self.N - 2)

    def print_map(self):
        """Print the current map of the game."""
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                elif (j, i) == (self.target_loc_x, self.target_loc_y):
                    print(" E ", end="")
                elif any((j, i) == (x, y) for x, y, _ in self.shots[-self.max_shots_displayed:]):
                    print(" * ", end="")
                else:
                    print(" . ", end="")
            print()

        print(f"Points: {self.points}")

    def move_targets(self):
        """Move the target every player move."""
        if self.target_move_countdown == 0:
            move_options = ["up", "down", "left", "right"]

            # Move the target
            direction = random.choice(move_options)
            new_x, new_y = self.move_in_direction(self.target_loc_x, self.target_loc_y, direction)

            if 0 <= new_x < self.N and 0 <= new_y < self.N:  # Check if the new position is within bounds
                self.target_loc_x, self.target_loc_y = new_x, new_y

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
        """Check if the coordinates (x, y) hit the target."""
        hit_target = (
                (x, y) == (self.target_loc_x, self.target_loc_y) or
                (abs(x - self.target_loc_x) <= 1 and abs(y - self.target_loc_y) <= 1)
        )

        if hit_target:
            self.hits += 1
            self.generate_new_target()
            self.target_move_countdown = 1
            self.points += 50  # +50 points for hitting the target
            print("Hit! +50 points")

        return hit_target

    def fire(self):
        """Fire a shot."""
        tank_direction = self.tank_direction
        shot_x, shot_y = self.tank_loc_x, self.tank_loc_y

        self.shots.append((shot_x, shot_y, tank_direction))
        self.total_shots += 1

        # Check if the shot hits the target
        if self.check_hit(shot_x, shot_y):
            pass  # Hit message is already printed in check_hit
        else:
            print("Miss!")

        # Deduct 10 points for each shot
        self.points -= 10

    def get_tank_direction(self):
        """Get the tank's current direction."""
        return self.tank_direction

    def left(self):
        """Move the tank left."""
        if self.tank_loc_x > 0:
            self.tank_loc_x -= 1
            self.tank_direction = "left"
            self.points -= 10

    def right(self):
        """Move the tank right."""
        if self.tank_loc_x < self.N - 1:
            self.tank_loc_x += 1
            self.tank_direction = "right"
            self.points -= 10

    def forward(self):
        """Move the tank forward."""
        if self.tank_loc_y > 0:
            self.tank_loc_y -= 1
            self.tank_direction = "up"
            self.points -= 10

    def back(self):
        """Move the tank backward."""
        if self.tank_loc_y < self.N - 1:
            self.tank_loc_y += 1
            self.tank_direction = "down"
            self.points -= 10

    def move_shots(self):
        """Move the shots independently."""
        new_shots = []
        for x, y, direction in self.shots:
            new_x, new_y = self.move_in_direction(x, y, direction)
            if 0 <= new_x < self.N and 0 <= new_y < self.N:  # Check if the new position is within bounds
                new_shots.append((new_x, new_y, direction))

        self.shots = new_shots

    def info(self):
        """Display information about the tank."""
        print(f"Tank Direction: {self.get_tank_direction()}")
        print(f"Tank Coordinates: ({self.tank_loc_x}, {self.tank_loc_y})")
        print(f"Total Shots: {self.total_shots}")
        print(f"Total Hits: {self.hits}")
        print(f"Points: {self.points}")
        print(f"Shots in Each Direction: {self.shots[-self.max_shots_displayed:]}")
        print(f"Target Coordinates: ({self.target_loc_x}, {self.target_loc_y})")

    def display_game_over(self):
        """Display 'Game Over' lettering in a framed style."""
        game_over_text = [
            "    GGG   A   M   M EEEEE  OOO  V   V EEEEE RRRR ",
            "   G     A A  MM MM E     O   O V   V E     R   R",
            "   G  GG AAAA M M M EEEE  O   O V   V EEEE  RRRR ",
            "   G   G A   A M   M E     O   O  V V  E     R  R ",
            "    GGG A   A M   M EEEEE  OOO    V   EEEEE R   RR",
        ]

        frame_width = len(game_over_text[0])  # Width without extra padding
        frame_line = "$" * frame_width

        print(frame_line)
        for line in game_over_text:
            print(f"{line}")
        print(frame_line)

    def game_over(self):
        """Handle game over."""
        self.display_game_over()

        # Collect game statistics
        game_stats = {
            "Moves": self.total_shots,
            "Shots": self.total_shots,
            "Hits": self.hits,
            "Score": self.points,
        }

        self.top_players.append(game_stats)

        # Display top players
        print("\nTop Players:")
        print(" Player |  Moves  |  Shots  |  Hits  |  Score")
        print("-------------------------------------------")
        for idx, stats in enumerate(sorted(self.top_players, key=lambda x: x["Score"], reverse=True)[:10], start=1):
            print(f" Player {idx} | {stats['Moves']:6}  | {stats['Shots']:6}  | {stats['Hits']:5}  | {stats['Score']:5}")

        # End the program
        exit()


    def play(self):
        """Play the Tank Game."""
        while self.points > 0:
            self.print_map()
            command = input("Input a command (left/l, right/r, forward/f, back/b, A/fire, info/i, quit/q): ")

            if command.lower() in ['left', 'l']:
                self.left()
            elif command.lower() in ['right', 'r']:
                self.right()
            elif command.lower() in ['forward', 'f']:
                self.forward()
            elif command.lower() in ['back', 'b']:
                self.back()
            elif command.lower() in ['fire', 'a']:
                self.fire()

            self.move_targets()
            self.move_shots()

            if command.lower() in ['info', 'i']:
                self.info()
            elif command.lower() in ['quit', 'q']:
                self.game_over()
            else:
                print("Invalid command. Please enter 'left', 'right', 'forward', 'back', 'A', 'quit'.")

        # Game Over if points reach 0 or less
        self.game_over()

if __name__ == "__main__":
    tg = TankGame()

    tg.play()

