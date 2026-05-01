# assaigment
# abdullahi hassan

#
username = input('who is this? ')
print('Welcome to our house :', username)
score = 0

# quiz 1
print('what is the capital city of somalia?: ')
answer_1 = input('')
if answer_1 == "mogadishu":
    print("correct!")
    score = +1
else:
    print("it is wrong")


# quiz 2
print('how many rivers are in somalia? ')
answer_2 = int(input())
if answer_2 == 2:
    print('correct!')
    score = +1
else:
    print('incorrect ')

# quiz 3
print('how many days of the week?')
answer_3 = input()
if answer_3 == '7' or answer_3 == 'seven':
    print('correct!')
    score = +1
else:
    print("incorrect ")
# final
print(username, 'you scored', score, 'out 3')

# PS C:\Users\hp\Desktop\Python Bootcamp>
# who is this? mr kalmoy
# Welcome to our house : mr kalmoy
# what is the capital city of somalia?:
# mogadishu
# correct!
# how many rivers are in somalia?
# 2
# correct!
# how many days of the week?
# 7
# correct!
# mr kalmoy you scored 2 out 3
