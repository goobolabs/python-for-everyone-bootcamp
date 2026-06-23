
# Initialize score
score = 0

# 1. Greeting
name = input("What is your name? ")
print("Welcome, " + name + "! Let's test your cybersecurity knowledge.\n")

# 2. Question 1
print("Q1: What does CIA stand for in cybersecurity?")
answer1 = input("Your answer: ").lower()

if answer1 == "confidentiality integrity availability" or answer1 == "cia":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. Correct answer: Confidentiality, Integrity, Availability.\n")

# 3. Question 2
print("Q2: What is used to protect a network from unauthorized access?")
answer2 = input("Your answer: ").lower()

if answer2 == "firewall":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. The correct answer is firewall.\n")


# 4. Final Score
print(name + ", you scored " + str(score) + " out of 2.")