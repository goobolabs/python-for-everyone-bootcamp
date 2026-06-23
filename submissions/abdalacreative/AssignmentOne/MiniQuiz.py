# Name: AbdalaCreative
# Description: Mini quiz program about Somali regions and their capitals

# Greeting
name = input("What is your name? ")
print("Welcome, " + name + "!\n")

# Score variable
score = 0

# Q1
print("Q1: What is the capital of Banaadir region?")
answer1 = input("Your answer: ").lower()

# Accept: mogadishu or muqdisho
if answer1 == "mogadishu" or answer1 == "muqdisho":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mogadishu.\n")

# Q2
print("Q2: What is the capital of Puntland (Bari region)?")
answer2 = input("Your answer: ").lower()

# Accept: bosaso or boosaaso
if answer2 == "bosaso" or answer2 == "boosaaso":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Bosaso.\n")

# Q3
print("Q3: What is the capital of Galguduud region?")
answer3 = input("Your answer: ").lower()


# Accept: dusamareb or dhuusamareeb
if answer3 == "dusamareb" or answer3 == "dhuusamareeb":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Dhuusamareeb.\n")

# Q4
print("Q4: What is the capital of Mudug region?")
answer4 = input("Your answer: ").lower()

# Accept: galdogob or galkacyo or gaalkacyo
if answer4 == "galkacyo" or answer4 == "gaalkacyo":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Galkacyo.\n")

# Q5
print("Q5: What is the capital of Awdal region?")
answer5 = input("Your answer: ").lower()

# Accept: borama
if answer5 == "borama":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Borama.\n")

# Final message
print(name + ", you scored " + str(score) + " out of 5.")