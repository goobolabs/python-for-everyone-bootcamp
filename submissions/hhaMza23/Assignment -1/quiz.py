
# Hamse Omer
# this is all answers for the  quiz 

User_Name = input("Please ENTER YOUR NAME : ? ")
print("welcomme, ", User_Name)

# Tracking variables
Score = 0
Total_Questions = 3


# Question 1
print("What is the capital of Saudi Arabia? ")
answer = input("Your answer: ") # Accepts only 'Riyadh' and 'riyadh'

if answer == "Riyadh" or answer == "riyadh":
    print("correct!!! the capital of Saudi Arabia is Riyadh..")
    Score += 1
else:
    print("Incorrect.. The capital of Saudi Arabia is Riyadh")


# Question 2
print("What is the second most beautiful city in saudi arabia ?")
answer = input("Your answer: ") # Accepts only 'Jeddah' and 'jeddah'

if answer == "Jeddah" or answer == "jeddah":
    print("Correct!! the second most beautiful city in saudi arabia is jeddah..")
    Score += 1
else:
    print("Incorrect!! the second most beautiful city in saudi arabia is jeddah.. ") 

# Question 3 
print("What is the official language of Saudi Arabia? ")
answer = input("Your answer: ") # Accept only 'Arabic' or 'arabic

if answer == 'Arabic' or answer == 'arabic':
    print("Correct!! The Official language of saudi arabia is arabic")
    Score += 1
else:
    print("Incorrect.. The official language of saudi arabia is arabic..")

print(User_Name, "You've scored ", Score, " out of", Total_Questions)




