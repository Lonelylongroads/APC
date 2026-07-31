#Python program to find largest of three numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Greater Number: ", a)
elif b >= a and b >= c:
    print("Greater Number: ", b)
else:
    print("Greater Number: ", c)
