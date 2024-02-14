class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


# Example usage:
temp = Temperature(0)  # Temperature initialized with 0 degrees Celsius
print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)

# Changing temperature in Celsius
temp.celsius = 100
print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)

# Changing temperature in Fahrenheit
temp.fahrenheit = 212
print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)
