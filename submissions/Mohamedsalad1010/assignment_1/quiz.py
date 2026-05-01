name = input("Enter your name: ")
print('Welcome', name)

score = 0

# question1
print( " 1) sheeg isku darka labadaan tiro: 12 + 20")
answer1 = input('your answer is :')
if answer1 == "32":
   print("correct\n")
   score +=1
else:
     print("Wrong! The correct answer  is 32\n")
     
# question2
print( "2) soomaaliye xagee ku taal  jawaabtaada ku qor soomaali ?")
answer2 = input('your answer is :').strip().lower()
if answer2 == "geeska africa":
   print("correct\n")
   score +=1
else:
     print("Wrong! The correct answer is  geeska africa\n")


# question3
print( "3) sheeg  natiijada isku dhufashada tirooyinkaan 10X3 ?")
answer3 = input('your answer is :').lower()
if answer3 == "30":
   print("correct\n")
   score +=1
else:
     print("Wrong! The correct answer is muqdisho\n")
     
#  finall result
print(name , "your score is" , score , "out of  3")