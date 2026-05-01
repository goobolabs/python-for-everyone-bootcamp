# user input 
user_input = input("Enter your name please: ")

if user_input.isalpha():
  print(f"Hello, {user_input}! Welcome to the quiz.")
else:
  print("Invalid input. Please enter a valid name consisting of letters only.")
  exit()  # Exit the program if the input is invalid

# question 1
question_1 = input("What is the capital of France? ")
score = 0
if question_1.lower().strip() == "paris":
    print("Correct!")
    score += 1
else:  
     print("Incorrect. The correct answer is Paris.")



# question 2
question_2 = input("What is the largest planet in our solar system? ")
if question_2.lower().strip() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Jupiter.")


# question 3 elif else
question_3 = input("What is the chemical symbol for water? ")
if question_3.lower().strip() == "h2o":
    print("Correct!")
    score += 1  
elif question_3.lower().strip() == "h20":
    print("Incorrect. The correct answer is H2O, not H20.") 
else:
    print("Incorrect. The correct answer is H2O.")    

print(f"Your final score is: {score}/3")