class Base:
    def __init__(self, age, cost, year_built, weight):
        self.age = age
        self.cost = cost
        self.year_built = year_built
        self.weight = weight

class SpaceShuttle(Base):
    def __init__(self, age, cost, year_built, weight, name):
        super().__init__(age, cost, year_built, weight)
        self.name = name

class MissionCalculator:
    FUEL_COST = 2  # Fuel cost per kg
    BURN_RATE = 0.1  # Burn rate in kg/mile
    BURN_RATE_VARIABLE = 2500

    def __init__(self, shuttle, orbit_height, personnel_count, base_salary):
        self.shuttle = shuttle
        self.orbit_height = orbit_height
        self.personnel_count = personnel_count
        self.base_salary = base_salary

    def calculate_fuel_cost(self):
        fuel_cost = self.FUEL_COST * self.BURN_RATE * (self.BURN_RATE_VARIABLE / self.orbit_height)
        return fuel_cost

    def calculate_personnel_expenditure(self):
        personnel_expenditure = self.personnel_count * self.base_salary
        return personnel_expenditure

    def calculate_mission_cost(self):
        fuel_cost = self.calculate_fuel_cost()
        personnel_expenditure = self.calculate_personnel_expenditure()
        total_cost = fuel_cost + personnel_expenditure
        return total_cost

    def get_full_report(self):
        report = f"Space Shuttle Info:\nName: {self.shuttle.name}\nAge: {self.shuttle.age}\nCost: {self.shuttle.cost}\nYear Built: {self.shuttle.year_built}\nWeight: {self.shuttle.weight}\n\n"
        report += f"Mission Cost Breakdown:\nFuel Cost: {self.calculate_fuel_cost()}\n"
        report += f"Personnel Expenditure: {self.calculate_personnel_expenditure()}\n"
        report += f"Total Mission Cost: {self.calculate_mission_cost()}\n"
        return report

# Sample Usage:

russian_shuttle = SpaceShuttle(age=10, cost=1000000000, year_built=2010, weight=100000, name="Russian Shuttle")
mission_calculator = MissionCalculator(russian_shuttle, orbit_height=300, personnel_count=10, base_salary=50000)
print(mission_calculator.get_full_report())
# Creating additional space shuttles
american_shuttle = SpaceShuttle(age=5, cost=2000000000, year_built=2015, weight=120000, name="American Shuttle")
chinese_shuttle = SpaceShuttle(age=3, cost=1500000000, year_built=2019, weight=110000, name="Chinese Shuttle")

# Sample Usage:

# Russian Shuttle
russian_shuttle = SpaceShuttle(age=10, cost=1000000000, year_built=2010, weight=100000, name="Russian Shuttle")
mission_calculator_russian = MissionCalculator(russian_shuttle, orbit_height=300, personnel_count=10, base_salary=50000)
print("Russian Shuttle Report:")
print(mission_calculator_russian.get_full_report())

# American Shuttle
mission_calculator_american = MissionCalculator(american_shuttle, orbit_height=300, personnel_count=10, base_salary=50000)
print("\nAmerican Shuttle Report:")
print(mission_calculator_american.get_full_report())

# Chinese Shuttle
mission_calculator_chinese = MissionCalculator(chinese_shuttle, orbit_height=300, personnel_count=10, base_salary=50000)
print("\nChinese Shuttle Report:")
print(mission_calculator_chinese.get_full_report())
