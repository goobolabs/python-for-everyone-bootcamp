# Student: Ali-Salad
# Description: A short text-based quiz about Python basics, with a randomized math question each run.

import random

# --- Greeting ---
name = input("What is your name? ")
print("Welcome, " + name + "!")

# Score starts at zero
score = 0

# -------------------------------------------------------
# Q1: Python keyword for output
# Accepted answers: "print" or "print()" (case-insensitive)
# -------------------------------------------------------
print("\nQ1: What keyword/function do you use to display text on the screen in Python?")
answer1 = input("Your answer: ").strip().lower()

if answer1 == "print" or answer1 == "print()":
    print("Correct!")
    score += 1
else:
    print("Not quite — the answer is: print")

# -------------------------------------------------------
# Q2: Python symbol for comments
# Accepted answers: "#" or "hash"
# -------------------------------------------------------
print("\nQ2: Which symbol is used to write a comment in Python?")
answer2 = input("Your answer: ").strip().lower()

if answer2 == "#" or answer2 == "hash":
    print("Correct!")
    score += 1
else:
    print("Not quite — the answer is: #")

# -------------------------------------------------------
# Q3: Randomized arithmetic expression (respects operator precedence)
# Three random digits (1-9) and randomly chosen operators are used.
# The correct answer is computed with eval() so it is always accurate.
# -------------------------------------------------------

# Pick three random single-digit numbers
a = random.randint(1, 9)
b = random.randint(1, 9)
c = random.randint(1, 9)

# Randomly choose the low-precedence operator (between the two groups)
outer_op = random.choice(["+", "-"])

# Randomly choose the high-precedence operator (evaluated first)
inner_op = random.choice(["*", "//"])

# Build the expression string, e.g. "3 + 5 * 2" or "7 - 4 // 2"
expression = str(a) + " " + outer_op + " " + str(b) + " " + inner_op + " " + str(c)

# Compute the correct answer using Python itself so it always matches
correct_answer = eval(expression)

print("\nQ3: What is the result of  " + expression + "  in Python?")
answer3 = input("Your answer: ").strip()

if answer3 == str(correct_answer):
    print("Correct! You remembered operator precedence.")
    score += 1

    # --- Nested / stretch follow-up question (only shown when Q3 is correct) ---
    print("\n  Bonus: Which rule explains why '" + inner_op + "' is evaluated before '" + outer_op + "'?")
    bonus = input("  Your answer: ").strip().lower()

    # Accept several valid phrasings
    if (bonus == "pemdas" or bonus == "bodmas"
            or bonus == "order of operations"
            or bonus == "operator precedence"):
        print("  Nice — you know your operator precedence rules!")
    else:
        print("  The term is 'operator precedence' (sometimes called PEMDAS/BODMAS).")
else:
    print("Not quite — remember that '" + inner_op + "' is evaluated before '"
          + outer_op + "', so  " + expression + "  =  " + str(correct_answer))

# --- Final result ---
print("\n" + name + ", you scored " + str(score) + " out of 3.")
