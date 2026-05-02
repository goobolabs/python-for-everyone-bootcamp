# Name: Aisha Abdullahi Mohamed
# quiz Assignment 1

score = 0
name = input("Enter Your Name:")
print("Hello Welcome,", name + "!")

#Q1
print ("\nQ1: What does IT stand for?")
q1 = input("Your answer: ").lower()
if q1 == 'information technology':
    print("correct")
    score +=1
else:
    print("Wrong answer!")


#Q2
print("\nQ2: What is Computer?")
print("A. Game")
print("B. Electronic machine")
print("C. phone")
q2 = input("your answer: (A\B\C) ").upper()
if q2 =="B":
    print("Correct")
    score +=1
else :
    print("Wrong answer!")


#Q3 
print("\nQ3: What is Software?")
print("A. Program")
print("B. Mouse")
print("C. Keyboard")

q3 = input("Your answer: (A\B\C) ").upper()
if q3 == "A":
    print("correct")
    score +=1
else:
    print("Wrong answer!")

#Q4
print("\nQ4: What are the main parts of a computer?")
q4 = input("Your answer: ").lower()

if q4 in ["cpu", "monitor", "keyboard" , "mouse"]:
    print("correct")
    score +=1
else:
    print('worng answer!')


#Final result
print("\nHi", name,"your score is " , score  ,"of 4")
if score >= 3:
    print("\nYour score is so good")
else:
    print("\nYou need more practice")