#Create a list of 10 numbers and display:
#First 5 elements
#Last 5 elements
#Middle 4 elements
#Alternate elements
#Reverse list using slicing

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 elements:", num[:5])
print("Last 5 elements:", num[-5:])
print("Middle 4 elements:", num[3:7])
print("Alternate elements:", num[::2])
print("Reversed list:", num[::-1])