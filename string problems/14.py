#Convert the first letter of every word to uppercase
s = input("write any sentence: ")
words = s.split()
title_cased = [w[0].upper() + w[1:] for w in words if w]
print(" ".join(title_cased))