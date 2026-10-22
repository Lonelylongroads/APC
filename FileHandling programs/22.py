with open("file1.txt", "w") as f:
    f.write("Hello from file 1\n")
with open("file2.txt", "w") as f:
    f.write("Hello from file 2\n")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
    f3.write(f1.read() + f2.read())