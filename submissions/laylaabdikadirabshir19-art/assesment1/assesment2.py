
name = input("layla ")
print("Welcome,", name + "!")

# Start score
score = 0
print("\nQ1: What keyword prints text in Python?")
q1 = input("hello world ")
if q1 == "print":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 'print'.")
print("\nQ2: What symbol is used for equality comparison in Python?")
q2 = input("correct: ")
if q2 == "==":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is '=='.")
print("\nQ3: Is Python case sensitive? (yes/no)")
q3 = input("no")

if q3 == "yes" or q3 == "y":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 'yes'.")

print("\n" + name + ", you scored", score, "out of 3.")