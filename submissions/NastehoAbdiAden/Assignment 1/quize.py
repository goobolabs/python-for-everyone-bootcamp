score = 0
print("--- The Mini Python Quiz ---")
user_name = input("What is your name? ")
print(f"Welcome, {user_name}! Let's see how much you know.\n")

# --- Question 1: Simple String Comparison ---
print("Q1: What is the keyword used to define a function in Python?")
answer1 = input("Your answer: ").strip().lower()

# I will accept 'def' as the only correct answer.
if answer1 == "def":
    print("Correct!")
    score += 1
else:
    print("Not quite! The answer is 'def'.")

print("-" * 20)

# --- Question 2: Logical Operators (Stretch Goal) ---
print("Q2: Is Python an interpreted language? (Yes or No)")
answer2 = input("Your answer: ").strip().lower()

# Using 'or' to accept multiple valid variations of the correct answer
if answer2 == "yes" or answer2 == "y":
    print("Spot on!")
    score += 1
else:
    print("Actually, it is interpreted!")

print("-" * 20)

# --- Question 3: Numbers and Comparison ---
print("Q3: How many space characters are recommended for one level of indentation in Python?")
answer3 = input("Your answer (use a number): ").strip()

# Check if the input is '4'. Note: input() returns a string, so we compare to "4".
if answer3 == "4":
    print("Exactly! PEP 8 style guide approves.")
    score += 1
else:
    print("The standard recommendation is 4 spaces.")

# --- Final Results ---
print("-" * 20)
print(f"Done! {user_name}, your final score is {score} out of 3.")

if score == 3:
    print("Perfect score! You're a Python pro.")
elif score > 0:
    print("Good job! You've got the basics down.")
else:
    print("Better luck next time!")