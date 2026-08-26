#Remove duplicate characters while maintaining the original order. 
s = input("write any sentence: ")
result = ""
for char in s:
    if char not in result:
        result += char
print(result)