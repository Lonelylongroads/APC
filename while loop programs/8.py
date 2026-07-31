#Python program to print Fibonacci series upto n

n = int(input("Enter a number for Fibonacci series: "))
a, b = 0, 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1