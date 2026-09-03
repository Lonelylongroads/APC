#Remove all duplicate elements while preserving the original order

num = [1, 2, 2, 3, 4, 3, 5, 1]
n = []

for i in num:
    if i not in n:
        n.append(i)

print(n)
