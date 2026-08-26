#Write a program to input a string and display its length without using the len() function. 
s = input("Write any sentence: ")
count = 0
for char in s:
    count += 1
print(count)