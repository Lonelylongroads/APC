#Python program to check whether the square root of number is prime or not
import math

num = float(input("Enter a number: "))
sqrt_num = math.isqrt(int(num)) if num >= 0 else 0

if num >= 0 and sqrt_num * sqrt_num == num and sqrt_num > 1:
    is_prime = True
    for i in range(2, int(math.isqrt(sqrt_num)) + 1):
        if sqrt_num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Square root ({sqrt_num}) is prime.")
    else:
        print(f"Square root ({sqrt_num}) is not prime.")
else:
    print("Square root is not an integer or is not prime.")