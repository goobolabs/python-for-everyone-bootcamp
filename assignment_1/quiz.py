# Ridwan
#  simple program about general question
name =input("what is your name?")
print("welcome!,", name,"let start question.\n")

score = 0
# question 1
print(" 1. what is 5 + 5")
answer1 = input("your answer:")

if answer1.lower() == "10":
    print("correct! .\n")
    score += 1
else:
    print("in coorect answer is 10.\n")

# question 2
print("2.what is the capitat city of awdal region?")

answer2 = input("your answer:")

if answer2.lower() == "borama":
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is borama. \n")

    #question 3
print("how many years do you learn in university?")
answer3 = input("your answer is:")

if answer3.lower() == "4years":
     print("correct!.\n")
     score += 1
else:
    print("incorrect answer is 4years.\n")
    
print("finished question")
print(name + ":your total score is", score, "out of3/3 ")







   








    