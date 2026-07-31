#Python program to find smallest of three numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a <= b and a <= c:
    print("Smaller Number: ", a)
elif b <= a and b <= c:
    print("Smaller Number: ", b)
else:
    print("Smaller Number: ", c)
