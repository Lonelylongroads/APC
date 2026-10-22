# Q. write python function to count the number of lines not starting with the alphabet 'T' from the given storage
def count_lines():
    count = 0
    with open("ps.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line and line[0] not in ("t"):
                count += 1
    return count


print(count_lines())