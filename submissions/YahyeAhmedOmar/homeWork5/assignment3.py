# journal.py

# This script uses one write operation first,
# then two append operations in the same script.

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Daily Journal\n")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Today I practiced Python.\n")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("I learned about append mode.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)