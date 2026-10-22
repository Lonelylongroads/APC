class Pers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Pers):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("Department:", self.department)
        print("Team Size:", self.team_size)


mrg = Manager("Sakshi", 28, "M202", 95000, "IT", 10)
mrg.display_manager_info()