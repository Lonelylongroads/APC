with open("attendance.txt", "w") as f:
    f.write("101, John, 32, 50\n")
    f.write("102, Emma, 45, 50\n")

with open("attendance.txt", "r") as f:
    for line in f:
        roll, name, attended, total = [p.strip() for p in line.split(",")]
        pct = (float(attended) / float(total)) * 100
        if pct < 75:
            print(name, f"{pct:.2f}%")