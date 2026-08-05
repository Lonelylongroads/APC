#Python program to print the smallest of n numbers
n = int(input("Enter total count of numbers: "))

if n > 0:
    smallest = float(input("Enter number 1: "))
    i = 1
    while i < n:
        num = float(input(f"Enter number {i + 1}: "))
        if num < smallest:
            smallest = num
        i += 1
    print("Smallest number:", smallest)
else:
    print("Invalid input count.")