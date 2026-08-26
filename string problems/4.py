#Check whether the entered string is a palindrome
s = input("write any sentence: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")