#Set
print("Example: Set using curly braces")
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days)
print(type(days))
print()

print("Looping through set elements: ")
for i in days:
    print(i)
print()

print("Example: Set using set() function")
days = set({"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"})
print(days)
print()

print("Looping through set elements: ")
for i in days:
    print(i)
print()

#adding elements to set
print("Adding elements to set...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print("Added month... ")
months.add("October")
print("Updated set: ")
print(months)
print()

#adding elements to set
print("Adding elements to set using update()...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
months.update({"July", "August", "September", "October"})
print("Updated set: ")
print(months)
print()

#removing elements to set
print("removing elements to set using set()...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print()
print("removing months... ")
print()
months.discard("January")
print("Modified set: ")
print(months)
print("looping through set elements...")
for i in months:
    print(i)

#second method
months.remove("February")
months.remove("March")
print("Modified set: ")
print(months)
print()

#third method
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print()
print("removing all months... ")
print()
months.clear()
print(months)
print()

#Union Operation
print("Applying Union Operation...")
d1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
d2 = {"Friday", "Saturday", "Sunday"}
print(d1|d2)
#second way
print()
print(d1.union(d2))
print()

#intersection Operation
print("Applying insertion Operation...")
d1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
d2 = {"Friday", "Saturday", "Sunday"}
print(d1&d2)
print()

#set methods
print("Applying set methods...")
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days)
print(type(days))
print()

for i in days:
    print(i)
print()

days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(days)
print()

months = {"January", "February", "March", "April"}
months.add("May")
print(months)
print()

months.update(["June", "July", "August"])
print(months)
print()

months.discard("August")
print(months)
print()

months.remove("July")
print(months)
print()

popped_month = months.pop()
print(popped_month)
print(months)
print()

copy_months = months.copy()
print(copy_months)
print()

months.clear()
print(months)
print()

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))
print(s1 | s2)
print()

print(s1.intersection(s2))
print(s1 & s2)
print()

print(s1.difference(s2))
print(s1 - s2)
print()

print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print()

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6}

set_a.intersection_update(set_b)
print(set_a)
print()

set_a = {1, 2, 3, 4, 5}
set_a.difference_update(set_b)
print(set_a)
print()

set_a = {1, 2, 3, 4, 5}
set_a.symmetric_difference_update(set_b)
print(set_a)
print()

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {6, 7, 8}

print(x.issubset(y))
print(x <= y)
print()

print(y.issuperset(x))
print(y >= x)
print()

print(x.isdisjoint(z))
print()