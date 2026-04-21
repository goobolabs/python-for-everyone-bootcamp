#Greating
name = input("What is your name? ")
print("Hello " + name + " welcome to the quiz")

score = 0

# Q1
print("\nQ1: What is 2 + 3 ?")
answer1 = input("Your answer: ")
if answer1 == "5":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 5.")

# Q2
print("\nQ2: What is 10 + 5 ?")
answer2 = input("Your answer: ")
if answer2 == "15":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 15")

# Q3
print("\nQ3: What is 9 + 1 ?")
answer3 = input("Your answer: ")
if answer3 == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 10")

# Q4
print("\nQ4: What is 7 + 8 ?")
answer4 = input("Your answer: ")
if answer4 == "15":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 15")

# final Score
print("\n", name, ", you scored", score, "out of 4")