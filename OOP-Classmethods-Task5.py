class SpaceStation:
    def __init__(self):
        self.astronauts = []

    def add_astronaut(self, name, nationality, mission_duration):
        astronaut = {
            'name': name,
            'nationality': nationality,
            'mission_duration': mission_duration
        }
        self.astronauts.append(astronaut)

    def find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                return astronaut
        return None

    @classmethod
    def from_astronaut_list(cls, astronaut_list):
        space_station = cls()
        space_station.astronauts = astronaut_list
        return space_station

    @staticmethod
    def is_long_term_mission(astronaut):
        return astronaut['mission_duration'] > 6

    def remove_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                self.astronauts.remove(astronaut)
                break

astronaut_list = [
    {'name': 'John Doe', 'nationality': 'USA', 'mission_duration': 8},
    {'name': 'Jane Smith', 'nationality': 'Canada', 'mission_duration': 5}
]

station = SpaceStation.from_astronaut_list(astronaut_list)

station.add_astronaut('David Johnson', 'UK', 7)

print(station.astronauts)

print(station.find_astronaut('John Doe'))

print(SpaceStation.is_long_term_mission({'name': 'John Doe', 'nationality': 'USA', 'mission_duration': 8}))

station.remove_astronaut('John Doe')

print(station.astronauts)

# under