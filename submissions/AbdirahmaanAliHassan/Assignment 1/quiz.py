# Name: Abdirahmaan
# Program: Simple Python Quiz (Assignment 1)

# score-ka bilow
score = 0

# 1. Magaca user-ka
name = input("What is your name? ")
print("Welcome,", name, "!\n")

# 2. Su'aasha 1
# Waxaan aqbaleynaa "print" ama "Print"
answer1 = input("Q1: What keyword prints text to the screen? ")

if answer1 == "print" or answer1 == "Print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'print'.\n")

# 3. Su'aasha 2
# Waxaan aqbaleynaa "input"
answer2 = input("Q2: Which is a city  of somalia? ")

if answer2 == "Mogadishu":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'input'.\n")

# 4. Su'aasha 3
# Waxaan aqbaleynaa "if"
answer3 = input("Q3: Which keyword is used for conditions in Python? ")

if answer3 == "if":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'if'.\n")

# 5. Natiijada ugu dambeysa
print(name + ", you scored " + str(score) + " out of 3.")