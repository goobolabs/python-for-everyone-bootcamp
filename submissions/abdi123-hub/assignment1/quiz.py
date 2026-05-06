# Abdul - Simple Python Quiz Program

# Ask name
name = input("What is your name? ")
print("Welcome, ", name + "!")

# Total questions
total_questions = 3
score = 0

print("I will ask you three questions. Try your best!\n")

# Question 1
Q1 = input("Q1: What keyword prints text to the screen? ")
if Q1 == "print" or Q1 == "Print":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 2
Q2 = input("Q2: What keyword is used to take input from the user? ")
if Q2 == "input" or Q2 == "Input":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 3
Q3 = input("Q3: What symbol is used for comments in Python? ")
if Q3 == "#" or Q3 == "hash" or Q3 == "Hash": 
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Final result
print(name + ", you scored", score, "out of", total_questions)
