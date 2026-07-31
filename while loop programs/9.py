#Python program to print factorial of given number


a = int(input("Enter number to find factorial: "))
fact = 1
i = 1

while i <= a:
    fact = fact * i
    i += 1

print(fact)