#simple python quiz
print("simple quiz")
name = input("what is your name: ")
print("welcome" + " " +  name )

score = 0

#question 1
print("Q1: how many regions in somalia")
answer1 = input("your answer is: ")
if answer1 == "18":
    score+= 1
    print("correct")
else:
    print("wrong answer")

 #question2

print("Q2: what is the capital city of somalia")  
answer2 = input("answer: ") 
if answer2 == "muqdisho" or answer2 == "mogadishu":
    score+= 1
    print("correct")
else:
    print("wrong answer")    

#question3

print("Q3: how many rivers does somalia")  
answer3 = input("answer: ")  
if answer3 == "2":
    score+=1
    print("correct")
else:
    print("wrong answer")    



#final message 
print(name , "your score is " + str(score) + " out of 3")

