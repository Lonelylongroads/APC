#Python program to print sum of odd numbers upto n

n = int(input("Enter number: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 2

print(total)