#Write a program to find the largest and smallest number in a list without using max() or min()

num = [10, 30, 50, 20, 70, 60]
largest = num[0]
smallest = num[0]

for n in num:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest number:", largest)
print("Smallest number:", smallest)