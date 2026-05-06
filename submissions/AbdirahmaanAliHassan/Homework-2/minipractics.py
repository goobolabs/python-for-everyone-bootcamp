                # Arithmetic operators
# a = 11
# b = 5
# sum = a+b
# print("addition = ", sum)
# print("subs = ", a - b)
# print("multiple = ", a * b)
# print("division = ", a / b) # kani wuxu so celinay float oo fraction ayuu ka dhigaya isku qaybinta
# print("Floor division = ", a // b) #kana integer ayuu so celinaya
# print("module = ", a % b)
# print("power = ", a ** b)

# # Mini practice
# # 1- Set two number variables and print their sum (for example 3 and 4, then print 7).

# num1 = 3
# num2 = 4
# total = num1+num2
# print(total)

# # 2- Print the value of 10 // 3 on one line (see how // differs from / in the lesson table).

# num3 = 9
# num4 = 3

# result = ("floor division" , num3//num4)
# net = ("division" , num3/num4)

# print(result)
# print(net)

# # 3- Print "Hi! " three times in one expression using * on a string.
# greeting = "hi"
# print(greeting *3)


                            # Assignment operators
# score = 10
# print("start:", score)

# score += 5   # same as score = score + 5
# print("after += 5:", score)

# score *= 2
# print("after *= 2:", score)

# score -= 3
# print("after -= 3:", score)

# score //= 3
# print("after //=" ,score)

# # Remainder example
# n = 10
# n %= 3
# print("10 % 3 as remainder:", n)



# Mini practice

# 1-Set balance = 100. Subtract 25 using -=. Add 10 using +=. Print balance (you should see 85).

# balance = 100
# balance -= 25
# balance += 10
# print("the Ans is ", balance)

# # 2-Set word = "Hi". Use += to append " there". Print word.
# word = "Hi"
# word += " there"
# print(word)


                        # Comparison operators
# a = 7
# b = 10

# print(a == b)
# print(a != b)
# print(a < b)
# print(5 <= a <= 9)


#     # Mini practice
# # 1-Set score = 88. Print whether score is greater than or equal to 80 (print the True or False result).

# score = 88
# print(score >=80)

# # 2-Set name = "Ada". Print whether name is equal to "Ada" using ==.

# name ="Ada"
# print(name == "Ada")


                        # Logical operators
# age = 25
# has_id = True
# print(age >= 18 and has_id)

# age = 16
# has_id = True
# print(age >= 18 and has_id)

# score = 85
# print(score < 60 or score > 100)

# score = 120
# print(score < 60 or score > 100)

# ready = False
# print(not ready)


    # Mini practice
# 1- Set username = "alex" and logged_in = True. Print a single expression (using and and ==) that is True only when the username is "alex" and logged_in is True.

# username = "alex"
# loggedIn = True

# print (username == "alex") and (loggedIn == True)

# 2-Set day = "Saturday". Print whether it is a weekend day using or and two comparisons to "Saturday" and "Sunday". Change day to "Monday" and run again so you see False.

# day = "Saturday"
# print((day == "Saturday") or (day == "Sunday"))



                #if, elif, else
score = int(input("enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Below C"

print("Grade:", grade)


    # Mini practice
# 1-Set temperature = 30. If it is 25 or above, print "warm". Elif it is 15 or above, print "ok". Else print "cold".

temperature = 30
if temperature >=25:
    print("Warm")
elif temperature >=15:
    print("Ok")


#2 -In the lesson’s grade example, change score to 76, run the code, and check that the printed grade matches what you expect.

score = 76

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Below C"

print("Grade:", grade)


        # Nested conditions

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the show.")
    else:
        print("You need a ticket.")
else:
    print("Sorry, minors not allowed.")


    # Mini practice
# 1-Ask for a username with input(). If it is "admin", ask for a password; if the password is "secret", print "Access granted", else print "Wrong password". If the username is not admin, print "Unknown user" (do not ask for a password).

username = "admin"
password = "secret"

name = input("Enter your username: ")

if name == username:
    entered_password = input("Enter your password: ")
    
    if entered_password == password:
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")