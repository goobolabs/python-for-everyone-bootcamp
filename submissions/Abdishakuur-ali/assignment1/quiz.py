# abdishakuur ali daahir

# greating

name = (input("enter your name:"))
print("welcome your name is:",name)
score = 0
total_questions = 3
# q1
answ1 = (input('what is your the city of somaliland:'))
if answ1 == "hargeisa":
    print('wow correct answer')
    score += 1
else:
    print('you are not the correct broooh')

#   Q2 waa suaashi labaad
  
answ2 = (input("the and  is true when:"))
if answ2 == "the both conditionis true":
    print('you are correct ')
    score += 1
elif answ2 == "the one conditions is true":
    print('you are wrong ')


#   q3 waxaan waydinya suaal ah the largest  muslin population in the world

answ3 = (input)('enter the largest muslim in the world: ')
if answ3 == "indonosia":
    print('correct answ ')
    score += 1
elif answ3 == "somalia":
    print('wrong answ ')
print(name, "you have scored,", score, "out of", total_questions)
