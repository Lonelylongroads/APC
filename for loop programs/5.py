#Python program to sum the given sequence 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / n!
n = int(input("Enter a number: "))
total_sum = 1.0
fact = 1

for i in range(1, n + 1):
    fact *= i
    total_sum += 1 / fact

print("Sum of sequence:", total_sum)