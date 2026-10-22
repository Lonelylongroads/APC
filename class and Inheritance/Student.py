class Student:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called: {self.name} created")

    def display(self):
        print(f"Student Name: {self.name}")

    def __del__(self):
        print(f"Destructor called: {self.name} destroyed")

s1 = Student("Sakshi")
s1.display()
del s1