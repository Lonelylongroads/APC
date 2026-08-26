#Reverse the order of words in a sentence without changing the words themselves. 
#Example:
#Input: Python is easy
#Output: easy is Python
s = input("write any sentence: ")
words = s.split()
print(" ".join(words[::-1]))