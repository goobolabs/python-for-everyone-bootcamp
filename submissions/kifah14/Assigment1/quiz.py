# Kifah Abdi
# Description: This is a Mini Quiz Program that asks 3 questions.

# Step 1: Get the user's name
name = input("What is your name? ")
print(f"Welcome, {name}!")

# Step 2: Initialize the score
score = 0

# Question 1
q1 = input("What are the colors of the Somali flag? ")
if q1.lower() == "blue and white":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 2
q2 = input("What symbol is used for comments in Python? ")
if q2 == "#":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
q3 = input("Which function is used to get input from the user? ")
if q3.lower() == "input" or q3.lower() == "input()":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Final Conclusion
print(f"{name}, your final score is {score} out of 3.")