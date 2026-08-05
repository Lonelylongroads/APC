#Python program to check entered number is palindrome or not
num = int(input("Enter a number: "))
temp = abs(num)
reversed_num = 0

while temp > 0:
 digit = temp % 10
 reversed_num = (reversed_num * 10) + digit
 temp = temp // 10

if num >= 0 and num == reversed_num:
 print(f"{num} is a palindrome number.")
else:
 print(f"{num} is not a palindrome number.")