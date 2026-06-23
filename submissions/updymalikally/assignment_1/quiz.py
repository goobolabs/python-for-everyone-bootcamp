name = input("What is your name?")
print("Welcome", name)
score = 0
print("What is your hobby?")
Ans1 = input()
if Ans1 == "photographer":
 print("Correct")
 score += 1
else:
            print("Wrong Answer! Try again")
   
print("Where do you live?")
Ans2 = input()
if Ans2 == "somaliland":
            print("Correct")
            score += 1
else:
            print("Wrong Answer! Try Again")
print("What is the capital of Somaliland?")
Ans3 = input()
if Ans3 == "Hargeisa":
            print("Correct!")
            score += 1
else:
            print("Wrong Answer! Try again")           
            print(name, "you scored", score, "out of 3")