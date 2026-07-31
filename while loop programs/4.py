#Python program to print sum of Natural numbers upto n

n = int(input("Enter number: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print(total)