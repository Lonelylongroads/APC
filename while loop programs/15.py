#Python program to print the largest of n numbers
n = int(input("Enter total count of numbers: "))

if n > 0:
    largest = float(input("Enter number 1: "))
    i = 1
    while i < n:
        num = float(input(f"Enter number {i + 1}: "))
        if num > largest:
            largest = num
        i += 1
    print("Largest number:", largest)
else:
    print("Invalid input count.")