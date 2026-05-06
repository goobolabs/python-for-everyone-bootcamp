# while_input.py

text = ""

while text != "done":
    text = input("Type something: ")

    if text != "done":
        print("You typed:", text)

print("Goodbye!")