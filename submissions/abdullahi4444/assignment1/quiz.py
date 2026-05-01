# Name: Abdullahi
# Description: A simple text-based quiz program with 7 questions using Python basics and control flow

# Ask user name
name = input("What is your name? ")
print("Welcome,", name, "!\n")

# Initialize score
score = 0

# Question 1
print("Q1: What keyword prints text to the screen?")
answer1 = input("Your answer: ").lower()

if answer1 == "print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'print'.\n")

# Question 2
print("Q2: What symbol is used for comments in Python?")
answer2 = input("Your answer: ")

if answer2 == "#":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is '#'.\n")

# Question 3
print("Q3: Does 'if' statement check conditions? (yes/no)")
answer3 = input("Your answer: ").lower()

if answer3 == "yes" or answer3 == "y":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'yes'.\n")

# Question 4
print("Q4: What data type is used for numbers like 10, 20, 30?")
answer4 = input("Your answer: ").lower()

if answer4 == "int" or answer4 == "integer":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'int'.\n")

# Question 5
print("Q5: What function is used to get input from the user?")
answer5 = input("Your answer: ").lower()

if answer5 == "input":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'input'.\n")

# Question 6
print("Q6: Which operator is used to compare two values? (== or =)")
answer6 = input("Your answer: ")

if answer6 == "==":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is '=='.\n")

# Question 7
print("Q7: What keyword is used for a condition when the first is false?")
answer7 = input("Your answer: ").lower()

if answer7 == "else":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'else'.\n")

# Final result
print(name + ", you scored", score, "out of 7.")
