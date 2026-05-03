# su'aalaha la waydiinayo userka marka hore


score = 0


name = input("magacaa noo sheeg? ")
print("welome ", name)

print("ma xiisaynaysaa barashada python?")
answer1 = input("your answer: ")

if answer1 == "haa":
    print("correct")
    score += 1
else:
    print("wrong")
    score -= 1 

print("ma filaysaa inaad wax ka faaiidi?")
answer2 = input("your answer: ")

if answer2 == "haa":
    print("correct")
    score += 1 
else:
    print("wrong")
    score -= 1 

print("ma filaysaa inaad dhamaysan doonto bootcamp ka?")
answer3 = input("your answer: ")


if answer3 == "haa":
    print("correct")
    score += 1
else:
    print("wrong")
    score -= 1

print("your score is 3 out of ", score)
