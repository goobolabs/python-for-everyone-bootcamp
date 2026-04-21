name = input("What is your name? ")
print("Hello, " + name + "!")


#Questions
correct=0
wrong = 0
question1 = input("What is the capital city of Somalia? ")
if(question1.lower() == "mogadishu"):
    print("Correct!")
    correct += 1
else:
    print("Wrong!")
    wrong += 1

question2 = input("What is the capital city of Kenya? ")
if(question2.lower() == "nairobi"):
    print("Correct!")
    correct += 1
else:
    print("Wrong!")
    wrong += 1


question3 = input("What is the capital city of Ethiopia? ")
if(question3.lower() == "addis ababa"):
    print("Correct!")
    correct += 1        
else:
    print("Wrong!")
    wrong += 1


print(name, "You scored", correct, "out of 3")
  

