# name: ikraan22
# A simple quiz program that asks the user a series of questions and keeps tract of their score.

# Greeting
name = input("what is your name? ")
print("wellc0me, ", name + "!")

#score variable
score = 0
#questions 1
print("Q1: What is the capital of ingland?")
answer1 == input("a) London\nb) Paris\nc) Madrid\nd) Rome\n")
if answer1 == "a" or answer1 == "london":
    print("correct!")
    score += 1
else:
    print("wrong! the correct answer is a London")

#question 2
print("what is the capital city of kenya?")
answer2 = input("a) Nairobi\nb) Mombasa\nc) Kisumu\nd) Eldoret\n")
if answer2 == "a" or answer2 == "nairobi":
    print("correct!")
    score += 1
else:
    print("wrong! the correct answer is a Nairobi.")

#question 3
print("what is the capital city of ethopia?")
answer3 = input("a) Addis Ababa\nb) Gondar\nc) Bahir Dar\nd) Hawassa\n")
if answer3 == "a" or answer3 == "addis ababa":
    print("correct!")
    score += 1
else:
    print("wrong! the correct answer is a Addis Ababa.")
    
    #final results
    print(name + ", you scored", score, "out of 3.")
    


