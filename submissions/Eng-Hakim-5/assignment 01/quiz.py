#Eng Akim
#Name: [Eng Akim]
# Description: A simple interactive quiz program that tracks the user's score.

# 1. Greeting
name = input("Welcome! What is your name? ")
print(f"Hi {name}, let's see how much you know about technology!")

# 3. Score - Initialize integer variable
score = 0

# 2. At least three questions
# Question 1: Python Basics
print("\nQuestion 1: Which keyword is used to create a function in Python?")
ans1 = input("Your answer: ").lower().strip()

# Logic: Accepting 'def' as the correct answer
if ans1 == "def":
    print("Correct!")
    score += 1
else:
    print("Not quite! The answer is 'def'.")

# Question 2: Hardware (Stretch goal: using 'or' for multiple spellings)
print("\nQuestion 2: Does 'CPU' stand for Central Processing Unit? (yes/no)")
ans2 = input("Your answer: ").lower().strip()

# Logic: Accepting 'yes' or 'y' using 'or'
if ans2 == "yes" or ans2 == "y":
    print("Exactly!")
    score = score + 1
else:
    print("Actually, it does!")

# Question 3: Databases
print("\nQuestion 3: What does SQL stand for?")
ans3 = input("Your answer: ").lower().strip()

# Logic: Accepting the full term
if ans3 == "structured query language":
    print("Perfect!")
    score += 1
else:
    print("Close! It's Structured Query Language.")

# 4. Final message
print("\n--- Quiz Complete ---")
print(f"Great job, {name}!")
print(f"Your final score is: {score} out of 3")