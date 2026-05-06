# Barsane101 - Math Quiz Program
# This quiz uses a number from the user and performs math operations

name = input("What is your name? ")
print("Welcome,", name + "! Let's start the math quiz.\n")

score = 0

# Ask user for a number
num = int(input("Enter a number: "))

# Q1: Addition
print("\nQ1: What is 50 +", num, "?")
ans1 = input("Your answer: ")

if int(ans1) == 50 + num:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Answer is", 50 + num, "\n")

# Q2: Subtraction
print("Q2: What is 50 -", num, "?")
ans2 = input("Your answer: ")

if int(ans2) == 50 - num:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Answer is", 50 - num, "\n")

# Q3: Division (safe check)
print("Q3: What is 50 /", num, "?")

if num != 0:
    ans3 = input("Your answer: ")
    
    # allow decimal answers
    if float(ans3) == 50 / num:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Answer is", 50 / num, "\n")
else:
    print("Cannot divide by 0. Skipping question.\n")

# Q4: Multiplication
print("Q4: What is 50 *", num, "?")
ans4 = input("Your answer: ")

if int(ans4) == 50 * num:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Answer is", 50 * num, "\n")

# Q5: Power
print("Q5: What is 50 **", num, "?")
ans5 = input("Your answer: ")

if int(ans5) == 50 ** num:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Answer is", 50 ** num, "\n")

# Final score
print(name + ", your final score is", score, "out of 5.")


#outPut

#What is your name? Barsane
#Welcome, Barsane! Let's start the math quiz.

#Enter a number: 4

# Q1: What is 50 + 4 ?
# Your answer: 54
# Correct!

# Q2: What is 50 - 4 ?
# Your answer: 46
# Correct!

# Q3: What is 50 / 4 ?
# Your answer: 8 
# Wrong! Answer is 12.5 

# Q4: What is 50 * 4 ?
# Your answer: 200
# Correct!

# Q5: What is 50 ** 4 ?
# Your answer: 66
# Wrong! Answer is 6250000 

# Barsane, your final score is 3 out of 5.
