print("What is your name? ", end="")
name = input()

print(f"Welcome, {name}!")
print()

score = 0
total = 3

# Q1
print("Q1: What keyword prints text to the screen? ", end="")
answer1 = input().strip().lower()
if answer1 == "print":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: print")
print()

# Q2
print("Q2: Which symbol is used for comments in Python? ", end="")
answer2 = input().strip()
if answer2 == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: #")
print()

# Q3
print("Q3: What data type is True or False? ", end="")
answer3 = input().strip().lower()
if answer3 == "bool" or answer3 == "boolean":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: bool")
print()

# Final Score
print(f"{name}, you scored {score} out of {total}.")
