class Vehicle:
    def __init__(self, capacity, fare):
        self.capacity = capacity
        self.fare = fare

    def get_default_fare(self):
        return self.capacity * 100

    def display_info(self):
        print(f"Capacity: {self.capacity}")
        print(f"Default Fare: ${self.get_default_fare():.2f}")


class Bus(Vehicle):
    def __init__(self, capacity, fare):
        super().__init__(capacity, fare)

    def get_default_fare(self):
        return super().get_default_fare() * 1.1  # Adding 10% maintenance charge


class Taxi(Vehicle):
    def __init__(self, capacity, fare):
        super().__init__(capacity, fare)

    # Additional method for Taxi, e.g., for displaying taxi-specific information
    def display_taxi_info(self):
        print("Taxi Information:")
        self.display_info()


class Train(Vehicle):
    def __init__(self, capacity, fare):
        super().__init__(capacity, fare)

    # Additional method for Train, e.g., for announcing the next station
    def announce_station(self, station):
        print(f"Next station: {station}")


# Example Usage:
bus = Bus(50, 150)
print("Bus Information:")
bus.display_info()
print()

taxi = Taxi(4, 200)
taxi.display_taxi_info()
print()

train = Train(200, 100)
print("Train Information:")
train.display_info()
train.announce_station("Central Station")
