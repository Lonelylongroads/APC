#creating dictionary
emp={"Name": "Sakshi", "Age" : 20, "Salary" : 26000, "Company" : "TCS"}
print(type(emp))
print("Printing employee details...")
print(emp)
print()

#using dict()
emp=dict({"Name": "Sakshi", "Age" : 20, "Salary" : 26000, "Company" : "TCS"})
print(type(emp))
print("Printing employee details...")
print(emp)
print()

#accessing dictionary values
emp={"Name": "Sakshi", "Age" : 20, "Salary" : 26000, "Company" : "TCS"}
print(type(emp))
print("Printing employee details...")
print("Name: ", emp["Name"])
print("Age: ", emp["Age"])
print("Salary: ", emp["Salary"])
print("Company: ", emp["Company"])
print()

#Dictionary methods
print("Applying dictionary methods...")
emp = {"Name": "Sakshi", "Age": 20, "Salary": 26000, "Company": "TCS"}
print(emp.get("Name"))
print(emp.keys())
print(emp.values())
print(emp.items())
print()
emp.update({"Salary": 30000, "Designation": "Developer"})
print(emp)
print()
print(emp.pop("Company"))
print(emp)
print()
print(emp.popitem())
print(emp)
print()
emp.setdefault("City", "Mumbai")
print(emp)
print()
new_emp = emp.copy()
print(new_emp)
print()
emp.clear()
print(emp)
print()
keys = ["Name", "Age", "Salary"]
default_dict = dict.fromkeys(keys, None)
print(default_dict)
print()


#Functions
def input(n1, n2):
    print("number 1 is ", n1)
    print("number 2 is ", n2)
print("Call to function...")
input(50,30)
print()

#function without parameters
def greet():
    print("Hello, World!")
greet()
print()

#function with parameters
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Alice")
print()

#default arguments in function
def function(n1, n2 = 20):
    print("number 1 is: ", n1)
    print("number 2 is: ", n2)
print("Passing one argument...")
function(40)
print("Passing two arguments...")
function(50,30)
print()

#lambda function
print("Applying lambda function...")
def add(num):
    return num+4
print(add(6))