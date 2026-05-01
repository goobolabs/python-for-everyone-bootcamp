# miski abdikadir
# Description: A 3-question quiz on Basic islamic questions.
# 1. Greeting
name = input("Enter your name: ")
print("Welcome" , name)

score = 0
#  Question 1:  easy question
print("Q1: In islam, what is the first prophet of islam?")
ans1 = input("Your answer: ")

if ans1=="adam" or ans1=="Adam":
    print("Correct! masha alah")
    score += 1
else:
    print("Incorrect answer ")

print()

#  Question 2: who was the last prophet in islam?
print("Q2:  who was the last prophet in islam?")
ans2 = input("Your answer: ")

if ans2=="mohamed":
    print("masha alah you are right")
    score += 1
else:
    print("wrong answer")

print()

#  Question 3: prayer
print("Q3: how many prayers do muslims do every day?")
ans3 = input("Your answer: ")

if ans3=="five" or ans3=="5":
    print("Correct!")
    score += 1
else:
    print("try again")



# 5. Final Message
print(f"Quiz Complete, {name}!")
print(f"Your Final Score: {score} out of 3")

# Feedback based on score
if score == 3:
    print("Excellent! You have a strong knowledge in islamic")
elif score >= 1:
    print("Good job! You're on the right track.")
else:
    print("Keep learning! ")