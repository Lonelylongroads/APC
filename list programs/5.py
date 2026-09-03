#Create a list of student names. Remove:
#First student 
#Last student 
#A specific student by name
#Display the remaining list.

students = ["Sakshi", "Prajakta", "Suchita", "Apurvaa", "Siddhi"]
students.pop(0)
students.pop()
students.remove("Suchita")
print(students)