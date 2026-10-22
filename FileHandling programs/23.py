with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

identical = True
for idx, (l1, l2) in enumerate(zip(lines1, lines2), 1):
    if l1 != l2:
        print(f"Files differ at line {idx}")
        identical = False
        break
if identical and len(lines1) == len(lines2):
    print("Files are identical")
elif identical:
    print(f"Files differ at line {min(len(lines1), len(lines2)) + 1}")