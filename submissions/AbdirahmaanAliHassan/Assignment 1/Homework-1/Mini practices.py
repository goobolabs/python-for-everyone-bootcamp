# Mini Practice 1 about programming
#========================================
# 1-In your own words (on paper or in a note), finish this sentence: A program is …

#  Ans: A program is a set of instructions that tell a computer what to do.

# 2- Name one thing a phone app does that involves input, processing, and output (example:               messaging—typing is input, sending/processing, notification is output).

# Ans: Music app — selecting a song is input, the app processes the request, and playing the sound is output.

# 3- How does a program actually run step by step inside the computer?

#Mini Practice 2 about programs run
#==========================================
# 1-Change the + 5 to + 3 and predict the printed line before running.
score = 10
score = score + 3
print(score)

# 2-Add a line between the two assignments: print(score). Predict two lines of output (first line shows 10, second line still 15 after the addition)—run and confirm.
score = 10
print(score)
score = score + 5
print(score)

# 3- “Why does order of lines matter?”
#The order matters because the program runs line by line, so earlier lines affect later results.

#Mini Practice 3 about Pseudocode
#====================================
# 1-Write pseudocode only for: read a number, multiply it by 2, print the result.
# READ number
# SET result = number * 2
# PRINT result


# 2- Translate your pseudocode into Python and run it with one number you type (you may use input and int if you already peeked ahead, or hard-code a variable for this drill).
#number = int(input("Enter a number: "))
number = int(input("Enter a number: "))
result = number * 2
print(result)

# 3- Write pseudocode for: if the score is at least 50, print pass; else print keep practicing.
# READ score
# IF score >= 50 THEN
#     PRINT "pass"
# ELSE
#     PRINT "keep practicing"
# END IF


#Mini Practice 4 about what-is-python
# 1-Change the string to include your own first name.
name = "Abdirahman"
print(name)

# 2-Add a second print(...) line that prints the word Python three times in one string.

name = "ahmed"
print(name)

print("welcome to  Python")

#Mini Practice-5  about Installation
# 1- Run python3 --version (or python --version) and write the exact version string.
        # python 3.14.4

# 2- Open interactive Python and print your name. Confirm you see your name.

print("ahmed")
# output ahmed

#Mini Practice-7 about  variables
# 1-Create variables city and country with string values. Print them on one line separated by a comma.
city = "Hargeisa"
country = "Somalia"

print(city + ", " + country)

#2 - Create counter = 0. Add 1 to counter three times. Print counter (should be 3).
counter = 0

counter = counter + 1
counter = counter + 1
counter = counter + 1

print(counter)


#Mini Practice-8 about  data-type

# 1- Create one variable of each type (int, float, str, bool). Print each value and its type(...) on the same line.

score = 43
result = 44.5
name = "abdirahman"
IsAdult = True

print(score, type(score))
print(result, type(result))
print(name, type(name))
print(IsAdult, type(IsAdult))

# 2- Predict then run: what is type("42")? What is type(42)? Write one sentence explaining the difference.
    #t"42" is a string because it has double quotes, while 42 is an integer because it has no quotes.

#Mini Practice-9 about  data-type
# 1- Write a program that asks for two integers and prints their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print(total)

# 2- Ask for a float price with float(input(...)) and print the price with a label, e.g. Price: 9.5.
price = float(input("Enter price: "))
print("Price:", price)