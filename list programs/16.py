#Create a nested list storing:
#Student Name
#Roll Number
#Marks
#Display all student details
students = [
    ["Sakshi", 3, 85],
    ["Apurva", 99, 90],
    ["Suchita", 103, 78]
]
for i in students:
    print(f"Name: {i[0]}, Roll No: {i[1]}, Marks: {i[2]}")