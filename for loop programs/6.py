#Python program to compute the cosine series cos(x)=1-x^2 / 2! + x^4 / 4! - x^6 / 6! + ... + x^n / n!
import math

x_deg = float(input("Enter angle in degrees: "))
n = int(input("Enter number of terms (n): "))

x = math.radians(x_deg)
cos_sum = 0.0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    cos_sum += term

print("Computed cos(x):", cos_sum)