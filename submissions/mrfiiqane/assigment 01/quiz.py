# general question
name = input("what is your name? ")
print("welcome!", name, "let start question.\n")

score = 0


# question 1
print(" 1. what is 5 + 5 ")
answer1 = int(input("your answer:"))

if answer1 == 10:
    print("correct! .\n")
    score += 1
else:
    print("in correct answer is 10.\n")

# question 2
print(" 2. what is 5 - 5 ")
answer2 = int(input("your answer:"))

if answer2 == 0:
    print("correct! .\n")
    score += 1
else:
    print("in correct answer is 0.\n")


# question 3
print(" 3. what is the capital city of somalia? mogadishu, muqdisho or xamar ")
answer3 = input("your answer:")

if answer3.lower() == "mogadishu" or answer3.lower() == "xamar" or answer3.lower() == "muqdisho":
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is mogadishu. \n")


# question 4
print(" 4. how many years do you learn in university? 4 or 5? ")
answer4 = input("your answer is:")

if answer4.lower() == "4" or answer4.lower() == "four":
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is 4 years.\n")


# question 5
print(" 5. what is your name? ")
answer5 = input("your answer is:")
if answer5.lower() == name.lower():
    print("correct!.\n")
    score += 1
else:
    print("incorrect answer is", name, ".\n")


print("finished question")
print(name + ":your total score is", score, "out of5/5 ")



# output
# what is your name? maxamed
# welcome! maxamed let start question.

#  1. what is 5 + 5 
# your answer:10
# correct! .

#  2. what is 5 - 5 
# your answer:0
# correct! .

#  3. what is the capital city of somalia? mogadishu, muqdisho or xamar 
# your answer:mogadishu
# correct!.

#  4. how many years do you learn in university? 4 or 5? 
# your answer is:4
# correct!.

#  5. what is your name? 
# your answer is:maxamed
# correct!.

# finished question
# maxamed:your total score is 5 out of5/5 