# Name: Abdullahi Ibrahim
# Description: A simple text-based quiz program using input, print, and if statements

# Greeting
name = input("What is your name? ")
print("Welcome,", name + "!\n")

# Score variable
score = 0

# Question 1
print("Q1: What keyword is used to print text in Python?")
answer1 = input("Your answer: ")

# Accepts "print"
if answer1.lower() == "print":
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
print("Q3: Which data type is used for whole numbers? (int / float / string)")
answer3 = input("Your answer: ")

# Accepts "int"
if answer3.lower() == "int":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 'int'.\n")

# Final result
print(name + ", you scored", score, "out of 3.")
