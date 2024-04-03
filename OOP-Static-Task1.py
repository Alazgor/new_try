class TemperatureConverter:
    @staticmethod
    def kelvin_to_celsius(kelvin):
        """
        Convert temperature from Kelvins to Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        """
        Convert temperature from Kelvins to Fahrenheit.
        """
        return (kelvin - 273.15) * 9/5 + 32

# Example usage:
kelvin_temp = 300  # Example temperature in Kelvins
celsius_temp = TemperatureConverter.kelvin_to_celsius(kelvin_temp)
fahrenheit_temp = TemperatureConverter.kelvin_to_fahrenheit(kelvin_temp)

print(f"{kelvin_temp} Kelvins is equal to {celsius_temp:.2f} Celsius")
print(f"{kelvin_temp} Kelvins is equal to {fahrenheit_temp:.2f} Fahrenheit")
