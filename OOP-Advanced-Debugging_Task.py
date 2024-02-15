import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def greet_person(full_name):
    try:
        """Function greets a person given full name as a string"""
        first_name, last_name = full_name.split()
        print(f"Hello {first_name} {last_name}, How are you today?")
    except ValueError as e:
        logging.error(f"Error in greet_person function: {e}")
        print("An error occurred while greeting the person. Please provide a full name.")

greet_person("John")  # This will intentionally cause an error by passing only one name
