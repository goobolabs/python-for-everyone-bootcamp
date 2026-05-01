

    #    python quiz
# Name: Ismail Nouh Hudhuun
# Description: A simple text-based Python quiz using input, output, and branching

# Ask user's name
name = input("What is your name? ")
print("Welcome,", name + "!\n")

# Initialize score
score = 0

# Question 1
print("Q1: What keyword is used to print output in Python?")
answer1 = input("Your answer: ").lower()

# Accepts "print"
if answer1 == "print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'print'.\n")

# Question 2
print("Q2: What symbol is used for comments in Python?")
answer2 = input("Your answer: ")

# Accepts "#"
if answer2 == "#":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is '#'.\n")

# Question 3
print("Q3: Does Python use indentation to define blocks? (yes/no)")
answer3 = input("Your answer: ").lower()

# Accepts "yes" or "y"
if answer3 == "yes" or answer3 == "y":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'yes'.\n")

# Final result
print(name + ", you scored", score, "out of 3.")