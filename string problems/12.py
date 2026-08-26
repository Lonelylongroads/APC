#Find the longest word in a given sentence. 
s = input("write any sentence: ")
words = s.split()
longest = max(words, key=len) if words else ""
print(longest)