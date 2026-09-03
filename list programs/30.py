#Store patient names and ages using lists. Perform: 
#Add a patient
#Delete a patient
#Search a patient
#Display all patients
#Count total patients

names = ["Sakshi", "Suchita", "Apurva"]
ages = [20, 19, 21]

print("list of patients:")
print("Names:", names)
print("Ages:", ages)

names.append("Apurvaaa")
ages.append(25)
print()

print("Removing 'Apurva' from list..")
remove = "Apurva"
if remove in names:
    index = names.index(remove)
    names.pop(index)
    ages.pop(index)

search = "Suchita"
if search in names:
    idx = names.index(search)
    print(f"\nFound {search}, Age: {ages[idx]}")
else:
    print(f"\n{search} not found.")

print("\nPatient List: ")
for p_name, p_age in zip(names, ages):
    print(f"Patient: {p_name}, Age: {p_age}")

print("\nTotal patients:", len(names))