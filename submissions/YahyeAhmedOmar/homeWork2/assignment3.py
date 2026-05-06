# logic_permissions.py

age = int(input("Enter your age: "))
parent = input("Is a parent with you? (y/n): ")

if (age >= 13) or (age >= 10 and parent == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")