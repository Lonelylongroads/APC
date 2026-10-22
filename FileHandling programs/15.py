with open("source.py", "r") as src, open("cleaned.py", "w") as dest:
    for line in src:
        if not line.strip().startswith("#"):
            dest.write(line)