# Find common elements between two lists.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

l = list(set(l1) & set(l2))
print(l)