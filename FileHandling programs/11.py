with open("student.txt", "r") as f:
    words = f.read().split()
    if words:
        print("Longest word:", max(words, key=len))