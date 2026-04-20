user_name=input("what is your name:")
print('Hello,welcom',user_name)
print("welcom to History Quiz:")
start=int(input("tap 1 to start: "))
count=0
# answer keys
correct1=1960
correct2="Hassan Sheik mohamud"
correct3="mohamed abdulahi hassan"
correct4="George Washington"
correct5="Nelson Mandela"
correct6=1914
correct7=1918
correct8=1939
correct9=1945
correct10="Germany"
# start the quiz
if start==1:

  print("1. when did somalia became an indepedent country? :")
  answer1=int(input())
  if answer1==correct1:
    print("congratulation you correct the 1 question")
    count+=1
  else:
    print("sorry! you are wrong :")
  print("2.who was the first president of somalia that became 2 times president ?")
  answer2=input()
  if answer2==correct2:
    print(" congratulatin you are rigtht")
    count+=1
  else:
    print(" sory! you are wrong")
  print("3.who was the famous soamli leader of derwish movement? ")
  answer2=input()
  if answer2==correct3:
    print(" congratulatin you are rigtht")
    count+=1
  else:
    print("sorry! you are wrong")
  print("4.who was the first president of United State?")
  answer4=input()
  if answer4==correct4:
    print(" congratulation you are rigtht")
    count+=1
  else:
    print("sorry! you are wrong")
  print("5.who was the south african leader imrisoned for 27 years and later became president?")
  answer5=input()
  if answer5==correct5:
    print(" congratulations you are rigtht")
    count+=1
  else:
    print(" sorry! you are wrong")
  print("6.whe did the world war started?")
  answer6=int(input())
  if answer6==correct6:
      print(" congratulations you are rigtht")
      count+=1
  else:
    print(" sorry! you are wrong")
  print("7.whe did the world war ended?")
  answer7=int(input())
  if answer7==correct7:
      print(" congratulations you are rigtht")
      count+=1
  else:
    print(" sorry! you are wrong")
  print("8.when did the world war || started?")
  answer8=int(input())
  if answer8==correct8:
      print(" congratulations you are rigtht")
      count+=1
  else:
    print(" sorry! you are wrong")
  print("9.when did the world war || Ended?")
  answer9=int(input())
  if answer9==correct9:
      print(" congratulations you are rigtht")
      count+=1
  elif answer9!=correct9:
    print(" sorry! you are wrong")
  print("10.who started world war || ?")
  answer10=input()
  if answer10==correct10:
      print(" congratulations you are rigtht")
      count+=1
  else:
    print(" sorry! you are wrong")
  # printing the final result of the quize with user name
  print( user_name ,"you corrected ",count,"out of  10")
else: 
  print("you are out of quiz")

 






    