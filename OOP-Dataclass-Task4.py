# You are tasked with designing an advanced Employee Management System using Python data classes, functional programming
# operations, and various methods for analysis and manipulation of employee data.
# Employee Class:
# Create a data class named Employee to represent an employee. The class should have attributes for employee_id, name,
# age, salary, and department.
# Department Class: Create a data class named Department to represent a department. The class should have attributes
# for department_id, name, and employe (List[Employee]).
# # Add a method named average_salary that calculates and returns the average salary of employees in the department.
# EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple departments and employees.
# The class should have an attribute for departments (List[Department]).
# # Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
# Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees
# within that age range.
# Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
# Add a method named filter_employees_by_department that takes a department name and returns a list of employees in that
# department.
# Functional Operations:
# Utilize functional programming operations such as map, filter, and sorted where appropriate in the implementation of
# the methods. Demonstrate the use of these operations to enhance the readability and efficiency of your code.
# Test Cases:
# Create a sample dataset with multiple employees and departments to thoroughly test your system. Use the implemented
# methods to perform various analyses, such as calculating average salaries, sorting employees, and filtering employees by criteria.
# Create a flight ticketing mini system:
# The CLI should ask you to choose departure place and destination (minimum 5 cities) (Use dictionary to create
# a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different different aircraft (Airbus A330-300, A340-300
# ,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300). Every aircraft has different seat configuration (economy,
# business, first with different seat amount, seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated depending on aircraft type,
# departure time, and fuel consumption. (We can agree that flights that are departure earlier, has less seats and older,
# cost more). Use data classes and simple classes to achieve the result.

from dataclasses import dataclass
# from dataclasses import dataclass: This line imports the dataclass decorator from the dataclasses module.
# The dataclass decorator is used to simplify the creation of classes where you want to primarily store data.
from typing import List
# from typing import List: This line imports the List type hint from the typing module.
# It's used to specify that a variable or parameter should be a list containing elements of a specific type.
# @dataclass: This is a decorator that is used to define a data class. It automatically generates special methods
# like __init__, __repr__, and __eq__ based on the class attributes.
@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    salary: float
    department: str

@dataclass
class Department:
    department_id: int
    name: str
    employees: List[Employee]

    def average_salary(self) -> float:
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

@dataclass
class EmployeeManagement:
    departments: List[Department]

    def total_salary(self) -> float:
        return sum(sum(employee.salary for employee in department.employees) for department in self.departments)

    def get_employees_in_age_range(self, min_age: int, max_age: int) -> List[Employee]:
        return [employee for department in self.departments for employee in department.employees if min_age <= employee.age <= max_age]

    def sort_employees_by_salary(self) -> List[Employee]:
        return sorted((employee for department in self.departments for employee in department.employees),
                      key=lambda x: x.salary, reverse=True)
    def filter_employees_by_department(self, department_name: str) -> List[Employee]:
        return [employee for department in self.departments if department.name == department_name for employee in department.employees]

# Sample dataset
emp1 = Employee(1, "John Doe", 30, 50000.0, "HR")
emp2 = Employee(2, "Jane Smith", 35, 60000.0, "HR")
emp3 = Employee(3, "Alice Johnson", 28, 55000.0, "IT")
emp4 = Employee(4, "Bob Brown", 40, 70000.0, "IT")
emp5 = Employee(5, "Charlie Davis", 32, 65000.0, "Finance")

dept_hr = Department(1, "HR", [emp1, emp2])
dept_it = Department(2, "IT", [emp3, emp4])
dept_finance = Department(3, "Finance", [emp5])

management = EmployeeManagement([dept_hr, dept_it, dept_finance])

# Testing methods
print("Average salary in IT department:", dept_it.average_salary())
print("Total salary in the organization:", management.total_salary())

print("Employees aged between 30 and 35:")
for emp in management.get_employees_in_age_range(30, 35):
    print(emp.name)

print("Employees sorted by salary:")
for emp in management.sort_employees_by_salary():
    print(emp.name, emp.salary)

print("Employees in the IT department:")
for emp in management.filter_employees_by_department("IT"):
    print(emp.name)


# from dataclasses import dataclass: This line imports the dataclass decorator from the dataclasses module. The dataclass
# decorator is used to simplify the creation of classes where you want to primarily store data.
#
# from typing import List: This line imports the List type hint from the typing module. It's used to specify that a
# variable or parameter should be a list containing elements of a specific type.
#
# @dataclass: This is a decorator that is used to define a data class. It automatically generates special methods like
# __init__, __repr__, and __eq__ based on the class attributes.
#
# class Employee:: This line starts the definition of the Employee class.
#
# employee_id: int: This line declares an attribute employee_id of type int for the Employee class.
#
# name: str: This line declares an attribute name of type str for the Employee class.
#
# age: int: This line declares an attribute age of type int for the Employee class.
#
# salary: float: This line declares an attribute salary of type float for the Employee class.
#
# department: str: This line declares an attribute department of type str for the Employee class.
#
# @dataclass: This is another decorator used to define the Department class.
#
# class Department:: This line starts the definition of the Department class.
#
# department_id: int: This line declares an attribute department_id of type int for the Department class.
#
# name: str: This line declares an attribute name of type str for the Department class.
#
# employees: List[Employee]: This line declares an attribute employees of type List[Employee] for the Department class.
# It represents a list of Employee objects associated with the department.
#
# def average_salary(self) -> float:: This line defines a method named average_salary for the Department class.
# It calculates and returns the average salary of employees in the department.
#
# return total_salary / len(self.employees): This line calculates the average salary by dividing the total salary of all
# employees in the department by the number of employees.
#
# @dataclass: This decorator defines the EmployeeManagement class.
#
# class EmployeeManagement:: This line starts the definition of the EmployeeManagement class.
#
# departments: List[Department]: This line declares an attribute departments of type List[Department] for the
# EmployeeManagement class. It represents a list of Department objects managed by the system.
#
# def total_salary(self) -> float:: This line defines a method named total_salary for the EmployeeManagement class.
# It calculates and returns the total salary of all employees in the organization.
#
# def get_employees_in_age_range(self, min_age: int, max_age: int) -> List[Employee]:: This line defines a method named
# get_employees_in_age_range for the EmployeeManagement class. It takes minimum and maximum age parameters and returns
# a list of employees within that age range.
#
# def sort_employees_by_salary(self) -> List[Employee]:: This line defines a method named sort_employees_by_salary for
# the EmployeeManagement class. It returns a sorted list of employees by their salary in descending order.
#
# def filter_employees_by_department(self, department_name: str) -> List[Employee]:: This line defines a method named
# filter_employees_by_department for the EmployeeManagement class. It takes a department name parameter and returns a
# list of employees in that department.
#
# emp1 = Employee(1, "John Doe", 30, 50000.0, "HR"): This line creates an instance of the Employee class with specified
# attributes.
#
# dept_hr = Department(1, "HR", [emp1, emp2]): This line creates an instance of the Department class with specified
# attributes and a list of employees.
#
# management = EmployeeManagement([dept_hr, dept_it, dept_finance]): This line creates an instance of the
# EmployeeManagement class with a list of departments.
#
# print("Average salary in IT department:", dept_it.average_salary()): This line prints the average salary of employees
# in the IT department.
#
# for emp in management.get_employees_in_age_range(30, 35):: This line iterates over the list of employees within the
# specified age range and prints their names.
#
# for emp in management.sort_employees_by_salary():: This line iterates over the sorted list of employees by their
# salary and prints their names and salaries.
#
# for emp in management.filter_employees_by_department("IT"):: This line iterates over the list of employees in the IT
# department and prints their names.