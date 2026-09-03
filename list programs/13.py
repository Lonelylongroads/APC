# Accept 10 numbers and sort them in: 
#Ascending order
#Descending order
num = []

for i in range(10):
    n = float(input(f"Enter number {i + 1}: "))
    num.append(n)

ascending = sorted(num)
descending = sorted(num, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)