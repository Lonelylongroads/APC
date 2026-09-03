#Store 15 integers in a list. Count how many numbers are:
#Even 
#Odd
num = []

for i in range(15):
    n = float(input(f"Enter number {i + 1}: "))
    num.append(n)

even_count = 0
odd_count = 0

for n in num:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)