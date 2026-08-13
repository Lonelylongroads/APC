#break statement
print("Break Statement Example:")
for string in "Python Loops":
    if string == "L":
     break
    print ("Current letter:", string)
print()


#continue statement
print("Continue Statement Example:")
for string in "Python Loops":
    if string == "o" or string == "P" or string == "t":
     continue
    print("Current letter:", string)
print()


#pass statement
print("Pass Statement Example:")
def pass_example():
    for i in range(0,10):
     pass
    print("Good Bye!")
pass_example()
print()


#+ve indexing
print("Positive Indexing:")
str="JAVAPOINT"
print(str[0:])
print(str[1:5])
print(str[2:4])
print(str[:3])
print(str[4:7])
print()


#-ve indexing
print("Negative Indexing:")
str="JAVAPOINT"
print(str[-1])
print(str[-3])
print(str[-2:])
print(str[-4:-1])
print(str[-7:-2])
print(str[::-1])
print(str[-2])
print()


#string functions
print("String Functions...")
string="Hello World"
result=string.split()
print(result)
print()


#multiline string
print("Multiline String...")
a="""Welcome
DYPCET
2026 BATCH"""
print(a)
print()

A="HELLO"
print(A[0])
print()

s="Hello World"
print(type(s))
print(s[3])
print(s[0:4])
print()


#Slicing
print("Slicing Example:")
s = "Hello World"
print(type(s))
print(s[3])
print(s[0:4])
print(s[:6])
print(s[0:])
print(s[0:10:2])
print("Length of string is: ",len(s))
print('l' in s)
print('S' in s)
print('S' not in s)
print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace('H', 'S'))
print(s)
print(s.split(" "))
print(s.count("l"))
s1 = "Welcome to Python Programming"
s2 = s+s1
print(s2)
print(len(s2))
