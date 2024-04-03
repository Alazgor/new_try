# class Country:
#     def __init__(self, name, population, area):
#         self.name = name
#         self.population = population
#         self.area = area
#         self.is_big = self.check_if_big()
#
#     def check_if_big(self):
#         return self.population > 20000000 or self.area > 3000000
#
#     def compare_pd(self, other_country):
#         pd_this = self.population / self.area
#         pd_other = other_country.population / other_country.area
#
#         if pd_this < pd_other:
#             return f"{self.name} has a smaller population density than {other_country.name}"
#         elif pd_this > pd_other:
#             return f"{self.name} has a larger population density than {other_country.name}"
#         else:
#             return f"{self.name} and {other_country.name} have the same population density"
#
#
# # Example usage:
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)
#
# print(australia.is_big)  # Output: True
# print(andorra.is_big)    # Output: False
# print(andorra.compare_pd(australia))  # Output: "Andorra has a larger population density than Australia"

class Country:

    def __init__(self, country_name, population, area):
        self.population = population
        self.area = area
        self.country_name = country_name

    def is_big(self):
        if self.population >= 20000000 and self.area >= 3000000:
            return True
        else:
            return False

    def country_density(self):
        self.density = self.population / self.area
        return self.density

    def compare(self, other_country):
        if self.country_density() > other_country.country_density():
            return f"{self.country_name} has a LARGER population density than {other_country.country_name}"

        elif self.country_density() < other_country.country_density():
            return f"{self.country_name} has a SMALLER population density than {other_country.country_name}"

        else:
            return f"{self.country_name} has an EQUAL population density than {other_country.country_name}"

Lithuania = Country("Lithuania", 2800000, 65300)
Latvia = Country("Latvia", 1884000, 64589)

print(Lithuania.is_big())

print(Lithuania.compare(Latvia))