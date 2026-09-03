#Accept 10 numbers from the user and store them in a list. Calculate: 
#Sum
#Average
num = []

for i in range(10):
    n = float(input(f"Enter number {i + 1}: "))
    num.append(n)

total_sum = sum(num)
average = total_sum / 10

print("Sum:", total_sum)
print("Average:", average)