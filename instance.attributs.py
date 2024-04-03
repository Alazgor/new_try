# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it
# with @company.com at the end. Make sure the entire email is in lowercase.

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

# Create an instance of the Employee class
employee_info = Employee(first_name='John', last_name='Doe')

# Accessing the info attribute is not a valid syntax, so I'm using employee_info
print(employee_info.fullname())
print(employee_info.email())

