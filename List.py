#a simple list
print("Printing Simple List...")
l1 = [1, 2, "Python", "Program", 15.9]
l2 = ["Amy", "Ryan", "Henry", "Emma"]

print(l1)
print(l2)

print(type(l1))
print(type(l2))
print()


#+ve Indexing lists
print("Positive Indexing Lists")
l = [0, 1, 2, 3, 4, 5]

print(l[0:])
print(l[:])
print(l[2:4])
print(l[1:3])
print(l[:4])
print()


#-ve Indexing lists
print("Negative Indexing Lists")
l = [0, 1, 2, 3, 4, 5]

print(l[-1])
print(l[-3:])
print(l[:-1])
print(l[3:-1])
print()


#Iterating a list
print("Iterating a list...")
l=["John", "David", "James", "Jonathan"]
for i in l:
    print(i)
print()


#adding elements to list
print("Adding elements to list....")
l = []
print(type(l))
n = int(input("Enter number of elements in list: "))
for i in range(0,n):
    l.append(input("Enter items: "))
print("Printing list items...")
for i in l:
    print(i, end=" ")
print()
print()


#removing elements from list
print("Removing elements from list....")
l=[0, 1, 2, 3, 4]
print("Original list: ")
for i in l:
    print(i, end=" ")
l.remove(2)
print()
print("Modified list: ")
for i in l:
    print(i, end=" ")
print()
print()


#Concatenation of list
print("Concatenation of a list...")
l1=[12, 14, 16, 18, 20]
l2=[9, 10, 32, 54, 86]
print(l1)
print(l2)
l=l1+l2
print(l)
print()


#Repetition of list
print("Repetition of list")
l1=[12, 14, 16, 18, 20]
print(l1)
l=l1*2
print(l)
print()


#List Methods
print("List Methods:")
l=[10, 30, 20, 50, 40, 60]
print("List: ", l)
print("Type of an object:", type(l))
l.append(70)
print("70 is appended: ", l)
l.insert(2, 90)
print("90 is inserted: ", l)
l1=[100, 300, 400, 900]
l.extend(l1)
print("Extended list: ", l)
l.sort()
print("Sorted list: ", l)
l.reverse()
print("Reversed list: ", l)
l2=l.copy()
print("Copied list: ", l2)
l.pop()
print("List after popping single element: ", l)
l.remove(900)
print("900 removed: ", l)
l.append(900)
print("Appended list: ", l)
print()


#Count() method: tuple
print("Count() method: tuple")
t1=(0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
print(t1)
print(type(t1))
t2=('Python', 'Java', 'Python', 'Tpoint', 'Python', 'Java')
print(t2)
print(type(t2))
res=t1.count(2)
print("Count of 2 in T1 is: ", res)
res1=t2.count('Java')
res2=t2.count('Python')
print("Count of Java in T2 is: ", res1)
print("Count of Python in T2 is: ", res2)
print()


#Index() method: tuple
print("Index() method: tuple")
t=(0, 1, 2, 3, 2, 3, 1, 3, 2)
print(t)
print(type(t))
res=t.index(3)
print("Occurence of 3: ", res)
res=t.index(3,4)
print("Occurence of 3 after 4th index is: ", res)