# iam shakirr -simple quiz game with scoring 

name = input("enter your name :")
print ("Welcome " + name + ", let's go to the quiz.")

score = 0
# Question 1

print("1: which language are we learning?")
q1 = input(" your answer:" )

#expected answer : python

if q1 == "python":
    print ("Correct.")
    score +=1
else:
    print("wrong, the answer is python.")


# Question 2

print("2:what does CPU stands for?")
q2 = input("your answer: ")

# expected answer : central processing unit.

if q2 == "central processing unit":
    print("Correct.")
    score +=1
else:
    print("Wrong, the answer is central processing unit.")


# Question 3

print("3: is python case sensitive?(y/n)")
q3 = input("your answer: ")

# Expected answer : y or yes 

if q3 == "y " or q3 == "yes":
    print ("Correct!")
    score +=1
else:
    print("wrong, python is case sensitive. ")

# FINAL RESULT

print(name + " your final score is ", score, "out of 3")