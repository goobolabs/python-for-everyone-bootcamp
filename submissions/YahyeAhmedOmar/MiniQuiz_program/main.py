# Yahye Ahmed
# Simple Python quiz program using input, print, variables, and conditions

score = 0

name = input("What is your name? ")

print("Welcome,", name + "!")
print()

# Question 1
# Accepts: print
answer1 = input("Q1: What keyword prints text to the screen in Python? ")

if answer1 == "print":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")

print()

# Question 2
# Accepts: 8
answer2 = input("Q2: What is 5 + 3? ")

if answer2 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")

print()

# Question 3
# Accepts: y or yes
answer3 = input("Q3: Is Python a programming language? (y/yes) ")

if answer3 == "y" or answer3 == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")

print()

print(name + ", you scored", score, "out of 3.")