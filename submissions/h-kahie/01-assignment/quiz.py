# Magaca: [Hassan Kahie]
# Program: Quiz-ka Soomaaliya iyo Python

# Part 1: Magaca qofka
name = input("Enter your name: ")
print("Kusoo dhawoow madashan: ", name, "!")

# Quiz and score 
score = 0

# Quiz 1
print("Quiz 1")
q1 = input("Gobolka ugu weyn somalia: ")
if q1 == "bari":
    print("Legend waad sheegtay!")
    score += 1
else:
    print("Legend waan ka xumahay ma aadan sheegin!")

# Quiz 2
print("\nQuiz 2")
q2 = input("Gobolada soomaaliya imisa weeye? ")
if q2 == "18":
    print("Mashallah waad sheegtay!")
    score += 1
elif q2 == "19":
    print("Maaha bro, mid ayaad ku dartay!")
else:
    print("Isku day wacan balse ma aadan haleelin waa 18 gobol.")

# Quiz 3
print("Quiz 3")
q3 = input("Caasimada soomaaliya sheeg: ")
if q3 == "muqdisho":
    print("Sax waaye!")
    score += 1
else:
    print("Waa khaldan tahay, waa Muqdisho.")

# Quiz 4
print("Quiz 4")
q4 = input("Python ma fudud tahay (Haa/Maya)?: ")
if q4 == "haa":
    print("Haa sax, waa luuqad fudud!")
    score += 1
else:
    print("Waa laga yaabaa inay kugu yara adagtahay bilowga.")

# Result
print("Hambalyo!")
print(name + ", Final Score: " + str(score) + "/4")
