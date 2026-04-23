
# Assignment 3: Logical combinations    and, or, not

age = int(input("Enter your age: "))
parent_present = input("Is a parent or guardian with you? (y/n): ")

if age >= 13 or (age >= 10 and parent_present == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")
