#Store names of students present in class. Display:
#Total students
#Search a student's attendance
#Add a new student
#Remove an absent student

Students = ["Sakshi", "Bhumi", "Suchita", "Apurva"]
print(Students)
print("Total students:", len(Students))

search = "Bhumi"
if search in Students:
    print(f"{search} is present.")
else:
    print(f"{search} is absent.")

Students.append("Siddhi")
Students.remove("Bhumi")

print("Updated attendance list:", Students)