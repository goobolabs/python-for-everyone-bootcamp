
#Ibrahim Abdirashid, This program is a quiz about Somalia.

greetinMyFriend = input("What is your name? ")
print("Welcome ", greetinMyFriend)

score = 0

capitalofSomalia = input("What is the capital of Somalia? ")
whatIsThePrimaryLanguage = input("What is the primary language spoken in Somalia? ")
whatIsTheCurrency = input("What is the currency of Somalia? ")

if capitalofSomalia == "Mogadisho":
    score += 1
if whatIsThePrimaryLanguage == "Somali":
    score += 1
if whatIsTheCurrency == "Somali Shilling":
    score += 1

print(greetinMyFriend +" " + " your score is " + " " + str(score))