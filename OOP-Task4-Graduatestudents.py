class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int, major: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def get_student_id(self) -> int:
        return self.student_id

    def get_major(self) -> str:
        return self.major

    def __str__(self) -> str:
        return f"{super().__str__()} is a student of {self.major} major. Student id: {self.student_id}."


class GraduateStudent(Student):
    def __init__(self, name: str, age: int, student_id: int, major: str, program: str, advisor: str):
        super().__init__(name, age, student_id, major)
        self.program = program
        self.advisor = advisor

    def get_program(self) -> str:
        return self.program

    def get_advisor(self) -> str:
        return self.advisor

    def __str__(self) -> str:
        return f"{super().__str__()} Program: {self.program}, Advisor: {self.advisor}."


# Example usage:
person1 = Person("Alice", 30)
print(person1)

student1 = Student("Bob", 25, 12345, "Computer Science")
print(student1)

grad_student1 = GraduateStudent("Charlie", 27, 54321, "Electrical Engineering", "PhD", "Dr. Smith")
print(grad_student1)
