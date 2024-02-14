# You are tasked with designing an advanced Employee Management System using Python data classes, functional programming
# operations, and various methods for analysis and manipulation of employee data.
# Employee Class:
# Create a data class named Employee to represent an employee. The class should have attributes for employee_id, name,
# age, salary, and department.
# Department Class: Create a data class named Department to represent a department. The class should have attributes
# for department_id, name, and employe (List[Employee]).
# Add a method named average_salary that calculates and returns the average salary of employees in the department.
# EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple departments and employees.
# The class should have an attribute for departments (List[Department]).
# Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
# Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees
# within that age range.
# Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
# Add a method named filter_employees_by_department that takes a department name and returns a list of employees in that department.
# Functional Operations:
# Utilize functional programming operations such as map, filter, and sorted where appropriate in the implementation of
# the methods. Demonstrate the use of these operations to enhance the readability and efficiency of your code.
# Test Cases:
# Create a sample dataset with multiple employees and departments to thoroughly test your system. Use the implemented
# methods to perform various analyses, such as calculating average salaries, sorting employees, and filtering employees
# by criteria.
#
# from dataclasses import dataclass
# from typing import List
#
# @dataclass
# class Employee:
#     employee_id: int
#     name: str
#     age: int
#     salary: float
#     department: str
#
# @dataclass
# class Department:
#     department_id: int
#     name: str
#     employees: List[Employee]
#
#     def average_salary(self):
#         if self.employees:
#             total_salary = sum(emp.salary for emp in self.employees)
#             return total_salary / len(self.employees)
#         else:
#             return 0
#
# @dataclass
# class EmployeeManagement:
#     departments: List[Department]
#
#     def total_salary(self):
#         return sum(sum(emp.salary for emp in dept.employees) for dept in self.departments)
#
#     def get_employees_in_age_range(self, min_age: int, max_age: int):
#         return [emp for dept in self.departments for emp in dept.employees if min_age <= emp.age <= max_age]
#
#     def sort_employees_by_salary(self):
#         return sorted((emp for dept in self.departments for emp in dept.employees), key=lambda emp: emp.salary, reverse=True)
#
#     def filter_employees_by_department(self, department_name: str):
#         return [emp for dept in self.departments if dept.name.lower() == department_name.lower() for emp in dept.employees]
#
# # Test Cases:
#
# # Create some employees
# employee1 = Employee(1, "Alice", 30, 60000, "Engineering")
# employee2 = Employee(2, "Bob", 35, 70000, "Engineering")
# employee3 = Employee(3, "Charlie", 40, 80000, "HR")
#
# # Create departments
# engineering_dept = Department(1, "Engineering", [employee1, employee2])
# hr_dept = Department(2, "HR", [employee3])
#
# # Create an EmployeeManagement instance
# employee_management = EmployeeManagement([engineering_dept, hr_dept])
#
# # Test functionalities
# print("Average salary in Engineering department:", engineering_dept.average_salary())
# print("Total salary in the organization:", employee_management.total_salary())
# print("Employees aged between 30 and 40:", employee_management.get_employees_in_age_range(30, 40))
# print("Employees sorted by salary:", employee_management.sort_employees_by_salary())
# print("Employees in HR department:", employee_management.filter_employees_by_department("HR"))

from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    salary: int
    department: "Department"

    # def __lt__(self, other):
    # #     return self.salary < other.salary
    # in method return sorted(employees_by_salary)


@dataclass
class Department:
    department_id: int
    name: str
    employees: List[Employee]

    def average_salary(self):
        total_salaries = sum([employee.salary for employee in self.employees])
        if len(self.employees) == 0:
            return 0
        return total_salaries / len(self.employees)


@dataclass
class EmployeeManagement:
    departments: List[Department]

    def total_salary(self):
        total_salaries_departments = 0
        for department in self.departments:
            total_salaries = sum([employee.salary for employee in department.employees])
            total_salaries_departments = total_salaries_departments + total_salaries
        return total_salaries_departments

    def get_employees_in_age_range(self, min_age, max_age):
        age_range_employees = []
        for department in self.departments:
            for employee in department.employees:
                if min_age <= employee.age <= max_age:
                    age_range_employees.append(employee)
        return age_range_employees

    def sort_employees_by_salary(self):
        employees_by_salary = []
        for department in self.departments:
            # employees_by_salary += department.employees
            employees_by_salary.extend(department.employees)
        return sorted(employees_by_salary, key=lambda x: x.salary, reverse=True)

    def filter_employees_by_department(self, department_name: str):
        for department in self.departments:
            if department.name == department_name:
                return department.employees





"""
EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple departments and employees. 
The class should have an attribute for departments (List[Department]).

Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees 
within that age range.
Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
Add a method named filter_employees_by_department that takes a department name and returns a list of employees in that 
department.

"""

emp1 = Employee(1, "Tom", 25, 1500, None)
emp2 = Employee(2, "Tim", 27, 1855, None)
emp3 = Employee(3, "John", 66, 2000, None)
emp4 = Employee(4, "Sam", 55, 2500, None)

dep1 = Department(11, "IT", [emp1, emp2])
dep2 = Department(12, "Finance", [emp3, emp4])

empmng = EmployeeManagement([dep1, dep2])
print(empmng.get_employees_in_age_range(15, 28))
print(empmng.sort_employees_by_salary())
print(empmng.filter_employees_by_department("IT"))

print(dep1.average_salary())
print(empmng.total_salary())