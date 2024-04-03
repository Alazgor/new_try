class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employees):
        """
        Calculate the total amount to be paid to all employees.
        """
        total_payroll = sum(employee.salary for employee in employees)
        return total_payroll

# Example usage:
employee1 = Employee("Alice", 3000)
employee2 = Employee("Bob", 4000)
employee3 = Employee("Charlie", 3500)

employees_list = [employee1, employee2, employee3]

total_payroll = Employee.calculate_payroll(employees_list)
print(f"The total payroll for all employees is ${total_payroll}.")
