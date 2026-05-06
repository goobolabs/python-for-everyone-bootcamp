# abdullahi (cigaalo9)
# Simple Python quiz program using input, print, variables, and if statements

# Score starts at 0
score = 0

# Ask for the user's name
name = input("What is your name? ")

# Welcome message
print(f"\nWelcome, {name}!")
print("Let's start the quiz!\n")

# Question 1
# Accepts: print
answer1 = input("Q1: What Python keyword is used to display text on the screen? ")

if answer1.lower() == "print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is print.\n")

# Question 2
# Accepts: if
answer2 = input("Q2: Which keyword is used to make decisions in Python? ")

if answer2.lower() == "if":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is if.\n")

# Question 3
# Accepts: y or yes
answer3 = input("Q3: Is Python a programming language? ")

if answer3.lower() == "yes" or answer3.lower() == "y":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is yes.\n")

# Final score message
print(f"{name}, you scored {score} out of 3.")