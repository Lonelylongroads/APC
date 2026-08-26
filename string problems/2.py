#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
s = input("write any sentence: ")
vowels = consonants = digits = spaces = special = 0
for char in s:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)