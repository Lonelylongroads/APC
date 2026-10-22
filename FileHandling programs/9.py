with open("student.txt", "r") as f:
    text = f.read().lower()
    vowels = 0
    consonants = 0
    for char in text:
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)