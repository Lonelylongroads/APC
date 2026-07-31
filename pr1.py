print("My name is Sakshi K \nDYPCET \n")


print("Enter numbers to be swapped")

a = int(input())
b = int(input())

a, b = b, a

print("a =", a)
print("b =", b)


print("Enter number to find factorial: ")
c = int(input())

fact=1

for i in range(1,c+1):
    fact= fact * i

print(fact)


n = int(input("Enter a number for Fibonacci series: "))

d, e = 0, 1
for i in range(n):
    print(d, end=' ')
    d, e = e, d + e