# summarize_file.py

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

print("Number of lines:", len(lines))
print("Number of characters:", len(content))