#Find the shortest word in a sentence. 
s = input("write any sentence: ")
words = s.split()
shortest = min(words, key=len) if words else ""
print(shortest)