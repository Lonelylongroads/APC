#Python program to find the sum of digits of given number
num = int(input("Enter a number: "))
num = abs(num)
total_sum = 0

while num > 0:
 digit = num % 10
 total_sum += digit
 num = num // 10

print("Sum of digits:", total_sum)