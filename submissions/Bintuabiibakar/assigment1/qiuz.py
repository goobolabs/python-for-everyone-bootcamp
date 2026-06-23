score = 0
total_questions = 3

name = input("Magacaaga geli: ")
print("Ku soo dhawoow", name)

# Su'aal 1
answer1 = input("1. 20 + 30 waa imisa? ")
if answer1.lower() == "50":
    print("Sax!")
    score += 1
else:
    print("Qalad!")

# Su'aal 2
answer2 = input("2. 10 - 5 waa imisa? ")
if answer2 == "5":
    print("Sax!")
    score += 1
else:
    print("Qalad!")

# Su'aal 3
answer3 = input("3. Biyaha midab ma leeyihiin? (haa/maya) ")
if answer3.lower() == "maya":
    print("Sax!")
    score += 1
else:
    print("Qalad!")

# Final message
print("\nQuiz wuu dhamaaday!")
print(name + ", dhibcahaagu waa:", score, "out of", total_questions)