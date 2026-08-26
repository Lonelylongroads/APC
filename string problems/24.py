#Find the character with the highest frequency. 
s = input("write any sentence: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
most_frequent = max(freq, key=freq.get) if freq else ""
print(most_frequent)