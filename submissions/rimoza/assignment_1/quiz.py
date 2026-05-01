# Ridwan Mohamed Abdi - 21/06/2026 (rimoza)
# This is a simple quiz program that asks the user three
# questions about Somaliland and calculates their score based on their answers.

name = input("Please enter your name: ")
print("Hello, " + name + "! Welcome to the quiz")

question_1 = input("What is the capital of Somaliland? ")

# I accept both "Hargeisa" and "hargeisa" as correct answers
if question_1 == "hargeisa" or question_1 == "Hargeisa":
    print("Correct!")
else:
    print("Incorrect. The correct answer is Hargeisa.")


# I accept both "Berbera" and "berbera" as correct answers
question_2 = input("What is the best port in Somaliland or East Africa? ")

if question_2 == "berbera" or question_2 == "Berbera":
    print("Correct!")
else:
    print("Incorrect. The correct answer is Berbera.")

# I accept Borama, borama, Buroa, and buoraa as correct answers
question_3 = input("What is the second largest city in Somaliland? ")

if question_3 == "borama" or question_3 == "Borama":
    print("Correct! Borama is the second largest city and best city in Somaliland.")
elif question_3 == "buroa" or question_3 == "Buroa":
    print("Correct! Buroa is the second largest city and largest livestock city in Somaliland.")
else:
    print("Incorrect. The correct answer is Borama or Buroa.")


score = 0
if question_1 == "hargeisa" or question_1 == "Hargeisa":
    score += 1
if question_2 == "berbera" or question_2 == "Berbera":
    score += 1
if question_3 == "borama" or question_3 == "Borama" or question_3 == "buroa" or question_3 == "Buroa":
    score += 1

print("Your final score is: " + str(score) + "/3")