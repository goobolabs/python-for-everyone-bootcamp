name=input("What is your name:  ")
print("Welcome", name, " let's start short Quizez")

score=0

quiz1=input("Q1: What is the capital city of Somalia?   ")

if quiz1 == 'Muqdisho' or 'Mogadisho' :
    
    print("Correct \n")
    score+=1
else:
    print("Wrong answer")

quiz2=input("Q2:  What keyword prints text to the screen?  ")

if quiz2 == "print" or "Print":
    print("Correct \n")
    score+=1
else:
    print("Wrong answer")

quiz3_txt=input("Q3: What year was the first release of a Linux operating system?  ")
quiz3=int(quiz3_txt)
if quiz3 == 1991:
    print("Correct \n")
    score+=1
else: 
    print("Wrong answer")

print(name,", you scored ",score , " out of 3")
