#Find the second largest element in a list
num = [45, 12, 89, 3, 67, 24]

n = list(set(num))
n.sort()
print(num)
print("Second largest element:", n[-2])