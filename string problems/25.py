#Find the second most frequently occurring character. 
s = input("write any sentence: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_freq) > 1:
    print(sorted_freq[1][0])
else:
    print("None")