class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self._salary = salary

    def get_yearly_salary(self):
        return self._get_salary() * 12

    def _get_salary(self):
        return self._salary

    def get_name(self):
        return self.__name


employee = Employee("John", 4561)

print(employee._salary)

print(employee.get_yearly_salary())

print(employee._get_salary())

# print(employee.__name)

print(employee.get_name())
