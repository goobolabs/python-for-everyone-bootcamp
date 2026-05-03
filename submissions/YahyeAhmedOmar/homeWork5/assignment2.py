# write_note.py

with open("note.txt", "w", encoding="utf-8") as file:
    file.write("Python Notes\n")
    file.write("Learning file handling in Python.\n")

with open("note.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)