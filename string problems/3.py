#Reverse the given string without using built-in reverse functions
s = input("write any sentence: ")
rev = ""
for char in s:
    rev = char + rev
print(rev)