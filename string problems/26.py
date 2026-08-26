#Encrypt and decrypt a message using the Caesar Cipher algorithm. 
text = input("write any sentence: ")
shift = int(input("write any number: "))

encrypted = ""
for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        encrypted += chr((ord(char) - base + shift) % 26 + base)
    else:
        encrypted += char

decrypted = ""
for char in encrypted:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        decrypted += chr((ord(char) - base - shift) % 26 + base)
    else:
        decrypted += char

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)