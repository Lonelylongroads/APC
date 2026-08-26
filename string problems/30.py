#Check whether one string is a rotation of another. 
#Example:
#ABCD
#CDAB
#Output: Yes
s1 = input("write first sentence: ")
s2 = input("write second sentence: ")
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")