# Create two 3 × 3 matrices using nested lists and perform matrix addition

m1 = [
    [1, 2, 73],
    [4, 54, 6],
    [7, 28, 4]
]
m2 = [
    [9, 68, 43],
    [86, 5, 14],
    [6, 2, 34]
]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        result[i][j] = m1[i][j] + m2[i][j]

for row in result:
    print(row)