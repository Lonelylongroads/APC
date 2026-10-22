with open("student.txt", "r") as src, open("upper.txt", "w") as dest:
    dest.write(src.read().upper())