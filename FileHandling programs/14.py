old_word = "John"
new_word = "Jane"
with open("student.txt", "r") as f:
    content = f.read()
new_content = content.replace(old_word, new_word)
with open("student.txt", "w") as f:
    f.write(new_content)