# name: Soadmohamud
# Simple quiz program

user = input("Enter your name: ")
print("Hello", user)

points = 0

print("Question 1: What is the capital city of Somalia?")
q1 = input()

if q1 == "Mogadishu":
    print("Right answer")
    points = points + 1
else:
    print("Not correct")

print("Question 2: When did Somalia become independent?")
q2 = input()

if q2 == "1960":
    print("Right answer")
    points = points + 1
else:
    print("Not correct")

print("Question 3: What is 4 * 5?")
q3 = input()

if q3 == "20":
    print("Right answer")
    points = points + 1
else:
    print("Not correct")

print("Question 4: What is 7 * 6?")
q4 = input()

if q4 == "42":
    print("Right answer")
    points = points + 1
else:
    print("Not correct")

print("Question 5: Which word is used to show output in Python?")
q5 = input()

if q5 == "print":
    print("Right answer")
    points = points + 1
else:
    print("Not correct")

print(user, "your score is", points, "out of 5")
