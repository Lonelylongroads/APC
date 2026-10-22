import re

text = "My numbers are 10, 20, 30"

# 1. findall()
print("findall:", re.findall("[0-9]+", text))

# 2. compile()
pattern = re.compile("[0-9]+")
print("compile:", pattern.findall(text))

# 3. split()
print("split:", re.split(",", "Apple,Banana,Mango"))

# 4. sub()
print("sub:", re.sub("Java", "Python", "I like Java"))

# 5. escape()
print("escape:", re.escape("a+b"))

# 6. search()
result = re.search("[0-9]+", text)
print("search:", result.group())