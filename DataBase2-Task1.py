import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание соединения с базой данных
engine = create_engine('sqlite:///employees.db')

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Определение базового класса для маппинга объектов на таблицы базы данных
Base = declarative_base()

# Определение класса для таблицы "Employee"
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(DateTime)  # Добавление колонки birth_date
    position = Column(String)
    salary = Column(Float)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, first_name, last_name, birth_date, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"<Employee('{self.first_name}', '{self.last_name}', '{self.position}', {self.salary})>"


# Создание таблицы в базе данных (если она еще не существует)
Base.metadata.create_all(engine)



def add_employee(first_name, last_name, birth_date, position, salary):
    # Добавление нового сотрудника в базу данных
    employee = Employee(first_name=first_name, last_name=last_name, birth_date=birth_date, position=position, salary=salary)
    session.add(employee)
    session.commit()

def view_employees():
    # Просмотр всех сотрудников в базе данных
    employees = session.query(Employee).all()
    for employee in employees:
        print(employee)

def delete_employee(employee_id):
    # Удаление сотрудника из базы данных по его ID
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
    else:
        print("Сотрудник не найден")

def update_employee(employee_id, attribute, new_value):
    # Обновление атрибута сотрудника в базе данных по его ID
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        setattr(employee, attribute, new_value)
        session.commit()
    else:
        print("Сотрудник не найден")

if __name__ == "__main__":
    # Пример использования функций
    add_employee("John", "Doe", datetime.date(1985, 10, 15), "Developer", 50000.0)
    add_employee("Jane", "Smith", datetime.date(1990, 5, 20), "Manager", 60000.0)
    view_employees()
    delete_employee(1)
    update_employee(2, "salary", 65000.0)

from sqlalchemy import inspect

inspector = inspect(engine)
columns = inspector.get_columns('employees')
print("Columns in 'employees' table:")
for column in columns:
    print(column['name'], column['type'])
