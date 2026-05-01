# Marshaale (Muktar)
# A mini quiz program that ask user's sample questions and display their score based on answers eg you scored 3 out of 5.

# Intro
username = input("Welcome to quiz what is your name? ")
print("Hi welcome",username)

# Initialize score count state
score = 0

# 1
print("Which planet is known as the Red Planet?")
answer_one = input().lower()
if answer_one == 'mars':
    score += 1
    print('Correct')
else:
    print('Incorrect')

# 2
print("What is the capital city of Japan?")
answer_two = input().lower()
if answer_two == 'tokyo':
    score += 1
    print('Correct')
else:
    print('Incorrect')

# 3
print("Who invented the light bulb?")
answer_three = input().lower()

# multiple condition correct answer using or.
if answer_three == 'thomas edison' or answer_three == 'thomasedison':
    score += 1
    print('Correct')
else:
    print('Incorrect')

# 4
print("What is 15 + 27?")

# Prevent the program to crash deu to user input eg. "ali","" because you can not convert alphabetical letters string to number.
try:
    answer_four = int(input())
    if answer_four == 42:
        score += 1
        print('Correct')
    else:
        print('Incorrect')
except:
    print('Incorrect')

# 5
print("Which ocean is the largest in the world?")
answer_five = input().lower()

# multiple condition correct answer using or.
if answer_five == 'pacific ocean' or answer_five == 'pacificocean' or  answer_five == 'pacific':
    score += 1
    print('Correct')
else:
    print('Incorrect')

print(username,",You scored",score,"out of 5")