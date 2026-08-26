#Print all duplicate characters in a string
s = input("write any sentence: ")
seen = set()
duplicates = set()
for char in s:
    if char in seen:
        duplicates.add(char)
    seen.add(char)
print(" ".join(duplicates))