# author Hibo
# mini quiz to practice python basics, variables, input/output and conditions

# greeting the user

name = input("what is your name pls? ")
print("welcome,", name + "!")

#score
score = 0

# starting questions
# question1
print("\nQ1: which contenant does the somalia located?")
answer1 = input("your answer: ").lower() # accept lowercase for comparison
if answer1 == "africa":
    print("correct!")
    score +=1
else:
    print("wrong! the correct answer is 'africa'.")

# question2
print("\nQ2: which of theseis a python data type? (int, apple car)")
answer2 = input("your answer: ").lower() # accept 'int' as correct answer
if answer2 == "int":
    print("correct!")
    score += 1
else:
    print("wrong! the correct answer is 'int'.")

# question 3
print("/nQ3: what is 10 + 3?")
answer3 = input("your answer: ")
if answer3 == "13": # compare as string since input() returns a string
    print("correct!")
    score += 1
else:
    print("wrong! the correct answer is 13.")
# the result
print(f"\n{name}, your scored {score} out of 3.")


