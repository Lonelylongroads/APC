#Check whether two strings are anagrams
s1 = input("write first sentence: ")
s2 = input("write second sentence: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")