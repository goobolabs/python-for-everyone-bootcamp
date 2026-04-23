# general question
name = input("what is your name?")
print("welcome!", name, "let start question.\n")

score = 0

# question 1
print(" 1. what is 5 + 5")
answer1 = int(input("your answer:"))

if answer1 == 10:
    print("correct! .\n")
    score += 1
else:
    print("in correct answer is 10.\n")

# question 2
print("2.what is the capital city of somalia?")

answer2 = input("your answer:")

if answer2.lower() == "mogadishu":
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is mogadishu. \n")

    # question 3
print("how many years do you learn in university?")
answer3 = input("your answer is:")

if answer3.lower() == "4years":
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is 4years.\n")

print("finished question")
print(name + ":your total score is", score, "out of3/3 ")



# output
# what is your name?maxamed
# welcome! maxamed let start question.

#  1. what is 5 + 5
# your answer:10
# correct! .

# 2.what is the capital city of somalia?
# your answer:mogadisho
# incorrect answer is mogadishu. 

# how many years do you learn in university?
# your answer is:4
# incorrect answer is 4years.

# finished question
# maxamed:your total score is 1 out of3/3 