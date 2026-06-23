# Jaabir - Simple Quiz Program
# This program asks the user questions and gives a final score.

# Greeting
name=input("enter the your name:")
print("soo dhawoow",name)
# Score variable
score=0
#comments
#uestion1
print("questione=what is html")
answer=input("enter the answer:")
# Accept: html or hypertext markup language
if answer == "hypertext markup language" :
   print("correct")
   score=+1
else:
    print("incorect")
 #question2
print("question2=sheeg madaweynaha somalia:")  
answer=input("enter the answer:")
if answer== "hassan sheik"    or "hasan":
 print("correct") 
 score += 1
else:
   print("incorect")
   #question3
print("queation3:what is cpu?") 
answer=input("enter the answer:" )
# Accept: central processing unit
if answer=="centrel proccessing unit":
    print("correct") 
    score += 1
else:
   print("incorect")   
 # Final message
print("Quiz Finished!")
print(f"{name},Your Total Score is:{score}out of 3")