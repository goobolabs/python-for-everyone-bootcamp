name = "Sundus"
print("what is your name?", name)
print("Welcome, Sundus!")

score = 0
# Q1
if input("Q1: what keyword prints text?" ) == "print":
    score += 1
# Q2
if input("Q2: what symbol is for comments python?") == "#":
    score += 1
# Q3
if input("Q3: what is the text data type?") ==  "string":
    score +=1

print("Sundus you scored", score, "out of 3")
