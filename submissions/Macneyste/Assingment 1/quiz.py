# Macneyste
# This program is a simple Python quiz that asks questions and tracks the score.

name = input("What is your name? ").strip()
print("Welcome, " + name + "! Let's start the Python quiz.\n")

score = 0
total_questions = 5

# Question 1
print("Q1: What keyword is used to define a function in Python?")
answer1 = input("Your answer: ").strip().lower()

# Accept: def
if answer1 == "def":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'def'.\n")


# Question 2
print("Q2: What symbol is used for addition in Python?")
answer2 = input("Your answer: ").strip()

# Accept: +
if answer2 == "+":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is '+'.\n")


# Question 3
print("Q3: What data type is used to store text in Python?")
answer3 = input("Your answer: ").strip().lower()

# Accept: str or string
if answer3 == "str" or answer3 == "string":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'str' or 'string'.\n")


# Question 4
print("Q4: Which keyword is used to repeat code in a loop?")
answer4 = input("Your answer: ").strip().lower()

# Accept: for or while
if answer4 == "for" or answer4 == "while":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'for' or 'while'.\n")


# Question 5
print("Q5: What function is used to get the length of a list or string?")
answer5 = input("Your answer: ").strip().lower()

# Accept: len or len()
if answer5 == "len" or answer5 == "len()":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'len'.\n")


print(name + ", you scored " + str(score) + " out of " + str(total_questions) + ".")

if score == total_questions:
    print("Excellent work!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again.")
