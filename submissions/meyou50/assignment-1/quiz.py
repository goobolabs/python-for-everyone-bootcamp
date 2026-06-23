# quiz game program
name = input("what is your name? :")
print("welcome to the quiz game ", name)
#score variable to keep track of the player's score
score = 0

#question 1
print("what keyword prints text to the screen :")

# get the player's answer
quiz1 = input("jawaabta gali : ")

if quiz1 == "print":
    print("waa sax")
    score +=1
else:
    print("waa khalad")

#question 2
print("what symbol is used for comments in python :")

# get the player's answer
quiz2 = input("jawaabta gali : ")

if quiz2 == "#" or quiz2 == "\"\"\"":
    print("waa sax")
    score +=1
else:
    print("waa khalad")

#question 3
print("what is the result of 3 +2 :")

# get the player's answer
quiz3 = input("jawaabta gali : ")

if quiz3 == "5":
    print("waa sax")
    score +=1
else:
    print("waa khalad")

#question 4
print("is python easy to learn (yes or no) :")

# get the player's answer

quiz4 = input("jawaabta gali :").lower()

if quiz4 == "yes" or quiz4 == "y":
    print("waa sax")
elif quiz4 == "no" or quiz4 == "n":
    print("wrong")
else:
    print("please answer yes or no ")



print("quiz is over")

print("your score is ",score)