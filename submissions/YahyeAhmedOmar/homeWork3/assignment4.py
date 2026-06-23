# phonebook.py

phonebook = {
    "Ahmed": "061234567",
    "Yahye": "062345678",
    "Ali": "063456789"
}

print(phonebook.get("Ahmed", "unknown"))
print(phonebook.get("Hassan", "unknown"))

for name in phonebook:
    print(name)

print("----")

for name, number in phonebook.items():
    print(name, ":", number)