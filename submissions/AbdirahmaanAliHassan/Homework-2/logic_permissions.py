# Assignment 3: Logical combinations (and / or)

# 1. Asks the user for their age as an integer (input() and int(...)).
age = int(input("Enter Your Age: "))
print(age)

# 2. Asks whether a parent or guardian is with them, using a single letter answer: the user types y or n (compare the string to "y").

parent = input("Miyuu kula socda waalid? (y/n): ")

if parent == "y":
    print("Waalid wuu kula socdaa")
else:
    print("Waalid kuma socdo")


# 3. Prints "OK to enter" if this rule is satisfied: age is 13 or older, or (age is at least 10 and the parent answer is y). Otherwise prints "Sorry, not this time".
if (age >= 13) or (age >= 10 and parent == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")