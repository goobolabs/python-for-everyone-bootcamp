# Name: Abdiaziz Bishar 
# Description: A simple 3-question quiz about Python basics.

# 1. Greeting
name = input("What is your name? ")
print(f"Welcome to the Python Challenge, {name}! Let's see what you know.")
print("-" * 30)

# Initialize score
score = 0

# 2. Question One
print("Q1: Which function do we use to get information from the user?")
answer1 = input("Your answer: ")

# Using .lower() ensures "Input", "INPUT", and "input" are all correct
if answer1.lower() == "input":
    print("Correct! Nice start.")
    score += 1
else:
    print("Not quite! The answer is 'input()'.")

# 3. Question Two (Using 'or' for the stretch goal)
print("\nQ2: Is Python an 'interpreted' or 'compiled' language?")
answer2 = input("Your answer: ")

if answer2.lower() == "interpreted" or answer2.lower() == "both":
    print("Exactly! Python code is executed line-by-line.")
    score += 1
else:
    print("Actually, it's primarily an interpreted language.")

# 4. Question Three (Nested logic stretch goal)
print("\nQ3: What is the result of 2 + 2 * 2?")
answer3 = input("Your answer: ")

if answer3 == "6":
    print("Great job! You remembered the order of operations.")
    score += 1
elif answer3 == "8":
    print("Close! Remember, multiplication happens before addition.")
else:
    print("Not quite. The answer is 6.")

# 5. Final Message
print("-" * 30)
print(f"Thanks for playing, {name}!")
print(f"Your final score is: {score} out of 3.")

if score == 3:
    print("Perfect score! You're a Python pro.")