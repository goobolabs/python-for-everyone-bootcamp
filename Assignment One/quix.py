# Description: A simple quiz program with different questions using Python basics.

# Greeting
name = input("What is your name? ")
print(f"Welcome, {name}!\n")

# Score
score = 0

# Question 1
print("Q1: What data type is the number 10 in Python?")
answer1 = input("Your answer: ").lower()

# Accepts: int or integer
if answer1 == "int" or answer1 == "integer":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'int'.\n")

# Question 2
print("Q2: Which symbol is used for comments in Python?")
answer2 = input("Your answer: ")

# Accepts: #
if answer2 == "#":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is '#'.\n")

# Question 3
print("Q3: What function is used to get user input in Python?")
answer3 = input("Your answer: ").lower()

# Accepts: input or input()
if answer3 == "input" or answer3 == "input()":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'input()'.\n")

# Final message
print(f"{name}, you scored {score} out of 3.")