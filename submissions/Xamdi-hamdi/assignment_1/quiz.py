# quiz program

name=input('enter your name: ')
print('welcome ', name)
score=0
# question 1

print('question 1: ' + "goormee ayuu dhashay nabi muxamas NNKH ?")
ans1=input('Answer: ')
if ans1=='571':
    print('correct !!')
    score+=1
else:
    print('incorrect !!')

# question 2
print('question 2: ' + "sheeg khaliif kii 2aad ee islaamka ?")
ans2=input('Answer: ')
if ans2=='cumar binu khadaab':
    print('correct !!')
    score+=1
else:
    print('incorrect !!')

    # question 3
print('question 3: ' + "what is the result of 20 + 30?")
ans3=input('Answer: ')
if ans3=='50':
    print('correct !!')
    score+=1
else:
    print('incorrect !!')

       # question 4
print('question 4: ' + "what is the result of 20 / 5?")
ans4=input('Answer: ')
if ans4=='4':
    print('correct !!')
    score+=1
else:
    print('incorrect !!')

     # question 5
print('question 5: ' + "what is the result of 21 x 3?")
ans5=input('Answer: ')
if ans5=='63':
    print('correct !!')
    score+=1
else:
    print('incorrect !!')

print('you finishe the quiz !')

print(name,'you scored '+ str(score) + ' out of 5')

