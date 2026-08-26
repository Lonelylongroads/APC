#Count the frequency of every word in a paragraph. 
s = input("write any sentence: ")
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)