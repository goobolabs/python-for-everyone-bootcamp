# Name: Fartuun (or your GitHub username)
# Description: A simple quiz program that asks questions and calculates the score

# Greeting
name = input("What is your name? ")
print(f"Welcome, {name}!\n")

# Score variable
score = 0

# Question 1
print("Q1: What keyword prints text to the screen?")
answer1 = input("Your answer: ").lower()

# Accepts: print
if answer1 == "print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'print'.\n")

# Question 2
print("Q2: What symbol is used for comments in Python?")
answer2 = input("Your answer: ")

# Accepts: #
if answer2 == "#":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is '#'.\n")

# Question 3
print("Q3: Is Python a programming language? (yes/no)")
answer3 = input("Your answer: ").lower()

# Accepts: yes or y
if answer3 == "yes" or answer3 == "y":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'yes'.\n")

# Final message
print(f"{name}, you scored {score} out of 3.")
