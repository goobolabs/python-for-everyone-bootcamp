name = input("Enter Your Name: ")
print("Welcome " + name)

score = 0

q1 = input("how mutch: 1 + 1 = ? ")
if int(q1) == 2:
    score += 1


q2 = input("how mutch: 5 - 2 = ? ")
if int(q2) == 3:
    score += 1


q3 = input("how mutch: 3 * 2 = ? ")
if int(q3) == 6:
    score += 1


q4 = input("how mutch: 10 / 2 = ? ")
if float(q4) == 5:
    score += 1

print("You correct", score, "questions")
