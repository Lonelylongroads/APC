#Python program to print 1 2 4 8 16 32 ... n^2
n = int(input("Enter a number: "))

for i in range(n + 1):
    val = 2 ** i
    if val <= n ** 2:
        print(val, end=" ")
    else:
        break
print()