# Mukhtar-kaariye
# Simple python quiz program 

#Greeting
name = input("What is your name? ")
print("Hello, " + name + "! Let's start the quiz.\n")

# Score variable starts at 0
score = 0

# Q1
print("Q1: What is the smallest unit of a living organism?")
answer1 = input("Your answer: ")

# Accepts: cell or the cell
if answer1.lower() == "cell" or answer1.lower() == "the cell":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is The cell.")

print("Current score:", score)
print()

# Q2
print("Q2: Which organ is responsible for pumping blood around the body?")
answer2 = input("Your answer: ")

# Accepts: heart or the heart
if answer2.lower() == "heart" or answer2.lower() == "the heart":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is The heart.")

print("Current score:", score)
print()

# Q3
print("Q3: What type of blood cells protect the body from diseases?")
answer3 = input("Your answer: ")

# Accepts: white blood cells
if answer3.lower() == "white blood cells":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is White blood cells.")

print("Current score:", score)
print()

# Q4
print("Q4: Which gas is necessary for human respiration?")
answer4 = input("Your answer: ")

# Accepts: oxygen
if answer4.lower() == "oxygen":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Oxygen.")

print("Current score:", score)
print()

# Q5
print("Q5: What is the name of the body’s outer protective covering?")
answer5 = input("Your answer: ")

# Accepts: skin or the skin
if answer5.lower() == "skin" or answer5.lower() == "the skin":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is The skin.")

print("Current score:", score)
print()

# Final result
print(name + ", you scored " + str(score) + " out of 5.")
print("Quiz completed!")