#Python program to print sum of even numbers upto n

n = int(input("Enter number: "))
i = 0
total = 0

while i <= n:
    total += i
    i += 2

print(total)