#PS: Convert tuple into mutable
tuple = (10, 20, 30)
print("Original:", tuple)
print("Type:", type(tuple))
print("Memory Address:", id(tuple))

print("Converting to Mutable...")

mutable_list = list(tuple)

mutable_list[0] = 99

print("Updated List:", mutable_list)
print("Type:", type(mutable_list))
print("Memory Address:", id(mutable_list))
print()


#using concatenation
t1 = (1,2,3,"Python")
print("t1 =",t1)
print(type(t1))
print(id(t1))
print()
t2 = ("java","Hello World",12,15,20)
print("t2 =",t2)
print(type(t2))
print(id(t2))

t = t1 + t2
print("t = ",t)
print(type(t))
print(id(t))