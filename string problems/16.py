#Display the frequency of every character in a string
s = input("write any sentence: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
for char, count in freq.items():
    print(f"{char}: {count}")