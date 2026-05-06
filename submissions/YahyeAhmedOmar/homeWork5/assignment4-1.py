# safe_read.py

file_name = "sample.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Done with open attempt.")