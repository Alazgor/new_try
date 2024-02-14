from dataclasses import dataclass
from typing import Dict, List

# Define data classes for Aircraft and Flight
@dataclass
class Aircraft:
    model: str
    seat_configuration: Dict[str, int]  # {'economy': 200, 'business': 50, 'first': 20}
    seat_pitch: Dict[str, int]  # {'economy': 30, 'business': 40, 'first': 50}
    average_price: Dict[str, float]  # {'economy': 500, 'business': 1500, 'first': 3000}
    fuel_consumption: int  # in gallons per hour
    age: int  # in years

@dataclass
class Flight:
    departure_place: str
    destination: str
    departure_time: str
    aircraft: Aircraft

# Define a dictionary to represent the distance between cities
city_distance = {
    ('New York', 'Los Angeles'): 2475,
    ('New York', 'Chicago'): 740,
    ('New York', 'Miami'): 1090,
    ('New York', 'Houston'): 1410,
    ('New York', 'San Francisco'): 2565
}

# Define aircraft data
aircraft_data = {
    'Airbus A330-300': Aircraft('Airbus A330-300', {'economy': 250, 'business': 36, 'first': 8},
                                 {'economy': 32, 'business': 45, 'first': 60},
                                 {'economy': 600, 'business': 2000, 'first': 3500}, 100, 10),
    'Airbus A340-300': Aircraft('Airbus A340-300', {'economy': 270, 'business': 40, 'first': 12},
                                 {'economy': 31, 'business': 45, 'first': 60},
                                 {'economy': 550, 'business': 1800, 'first': 3200}, 120, 12),
    'Airbus A340-600': Aircraft('Airbus A340-600', {'economy': 300, 'business': 50, 'first': 14},
                                 {'economy': 33, 'business': 46, 'first': 62},
                                 {'economy': 520, 'business': 1700, 'first': 3100}, 130, 14),
    'Airbus A350-100': Aircraft('Airbus A350-100', {'economy': 280, 'business': 42, 'first': 10},
                                 {'economy': 32, 'business': 47, 'first': 61},
                                 {'economy': 580, 'business': 1900, 'first': 3300}, 110, 8),
    'Boeing 747-400': Aircraft('Boeing 747-400', {'economy': 350, 'business': 60, 'first': 16},
                                {'economy': 34, 'business': 48, 'first': 64},
                                {'economy': 500, 'business': 1600, 'first': 3000}, 150, 20),
    'Boeing 747-800': Aircraft('Boeing 747-800', {'economy': 380, 'business': 64, 'first': 18},
                                {'economy': 35, 'business': 50, 'first': 66},
                                {'economy': 480, 'business': 1500, 'first': 2900}, 160, 15),
    'Boeing 777-300': Aircraft('Boeing 777-300', {'economy': 320, 'business': 55, 'first': 15},
                                {'economy': 33, 'business': 49, 'first': 65},
                                {'economy': 550, 'business': 1700, 'first': 3100}, 140, 18),
}

# Define a function to calculate flight cost
def calculate_flight_cost(flight: Flight) -> float:
    distance = city_distance.get((flight.departure_place, flight.destination), 0)
    fuel_cost = distance * flight.aircraft.fuel_consumption
    time_cost = 10 - int(flight.departure_time.split(':')[0])  # Assume earlier departure time costs more
    age_cost = flight.aircraft.age * 100  # Assume older aircraft costs more
    total_cost = fuel_cost + time_cost + age_cost
    return total_cost

# Main function to interact with the user
def main():
    print("Welcome to the Flight Ticketing System!")
    print("Please choose your departure place:")
    for city in city_distance.keys():
        print(city[0])
    departure_place = input("Enter your departure place: ")
    print("Please choose your destination:")
    for city in city_distance.keys():
        print(city[1])
    destination = input("Enter your destination: ")

    # Display flight options
    print("Available flight options:")
    for aircraft_model, aircraft in aircraft_data.items():
        flight = Flight(departure_place, destination, "08:00", aircraft)  # Assume fixed departure time for simplicity
        flight_cost = calculate_flight_cost(flight)
        print(f"Aircraft: {aircraft_model}, Total Cost: ${flight_cost:.2f}")

if __name__ == "__main__":
    main()
