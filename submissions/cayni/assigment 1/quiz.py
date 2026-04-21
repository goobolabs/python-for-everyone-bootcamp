score = 0
total_questions = 3

name = input("Enter your name: ")
print("Welcome", name)

# Using for loop + range
for i in range(1, total_questions + 1):

    if i == 1:
        answer = input("1. add 3 + 2? ")
        if answer == "5":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    elif i == 2:
        answer = input("2. caasimada Somalia? ")
        if answer.lower() == "moqdisho":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    elif i == 3:
        answer = input("3. ma jeceshy python? (haa mize) ")
        
        # using OR (stretch)
        if answer.lower() == "haa":
            print("waa ficanthy lkn")
            score += 1

            # nested if (stretch)
            reason = input("maxa ku jecldatay? ")
            if reason != "":
                print("mahadsanid")
        else:
            print("Okay!")

# Final message
print("\nQuiz finished!")
print(name + ", your final score is:", score, "out of", total_questions)