class ImperialToMetricConverter:
    @staticmethod
    def inches_to_centimeters(inches):
        """
        Convert length from inches to centimeters.
        """
        return inches * 2.54

    @staticmethod
    def feet_to_meters(feet):
        """
        Convert length from feet to meters.
        """
        return feet * 0.3048

    @staticmethod
    def pounds_to_kilograms(pounds):
        """
        Convert weight from pounds to kilograms.
        """
        return pounds * 0.453592

    @staticmethod
    def miles_to_kilometers(miles):
        """
        Convert distance from miles to kilometers.
        """
        return miles * 1.60934

    @staticmethod
    def gallons_to_liters(gallons):
        """
        Convert volume from gallons to liters.
        """
        return gallons * 3.78541

# Example usage:
inches = 10
feet = 5
pounds = 150
miles = 25
gallons = 10

centimeters = ImperialToMetricConverter.inches_to_centimeters(inches)
meters = ImperialToMetricConverter.feet_to_meters(feet)
kilograms = ImperialToMetricConverter.pounds_to_kilograms(pounds)
kilometers = ImperialToMetricConverter.miles_to_kilometers(miles)
liters = ImperialToMetricConverter.gallons_to_liters(gallons)

print(f"{inches} inches is equal to {centimeters:.2f} centimeters")
print(f"{feet} feet is equal to {meters:.2f} meters")
print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms")
print(f"{miles} miles is equal to {kilometers:.2f} kilometers")
print(f"{gallons} gallons is equal to {liters:.2f} liters")
