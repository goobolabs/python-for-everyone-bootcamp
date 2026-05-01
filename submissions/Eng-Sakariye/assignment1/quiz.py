#Dev Muna
#This program is a simple Python quiz using input, print, and conditions

# Greeeting
name = input("What is your name? ")
print("Welcome, " + name)

Score = 0

# Question 1
print("Q1: What keyword is used to define a function in Python?")
Answer1 = input("Your answer: ")

if Answer1.lower() == "def":
    print("Correct!")
    Score += 1
else:
    print("Incorrect. The correct answer is 'def'.")


# Question 2
print("Q2: What symbol is used for addition in Python?")
Answer2 = input("Your answer: ")

if Answer2 == "+":
    print("Correct!")
    Score += 1
else:
    print("Incorrect. The correct answer is '+'.")


# Question 3
print("Q3: What data type is used to store text in Python?")
Answer3 = input("Your answer: ")

if Answer3.lower() == "str" or Answer3.lower() == "string":
    print("Correct!")
    Score += 1
else:
    print("Incorrect. The correct answer is 'str' or 'string'.")


# Question 4
print("Q4: Which keyword is used for a loop in Python?")
Answer4 = input("Your answer: ")

if Answer4.lower() == "for":
    print("Correct!")
    Score += 1
else:
    print("Incorrect. The correct answer is 'for'.")


# Question 5
print("Q5: What function is used to get the length of a list or string?")
Answer5 = input("Your answer: ")

if Answer5.lower() == "len":
    print("Correct!")
    Score += 1
else:
    print("Incorrect. The correct answer is 'len'.")