# variables
name = "abdinasir"
score = 0
score += 10
answer_1 = "agreculture"
answer_2 = "IT"
answer_3 = "health"

subject_1 = "python"
subject_2 = "anotomy and pysiology"
subject_3 = "forest and enviromental pototection"

color_1 = "black"
color_2 = "red"
color_3 = "blue"

# greeing

greeting = print(input("what is your name plz? "))
print("well come",name)
# question 1
question_1 = print(input("can you tell us your educational bacground ?"))
if  question_1 == answer_1:
        print("waaw ",answer_1,"isfine but ", answer_2, "is better")
       
elif question_1 == answer_2:
        print("great ",answer_2,"is very interasting")
else:
        print("that is good but why don't you  learn ",answer_2,"has good future in this modren technology ?")
print(score + 10)

# question 2

question_2 = print(input("what is your favorate subject ?"))
if question_2 == subject_1:
        print("waaw its interesting course")
elif question_2 == subject_3:
        print("it gives clear direction for citizen to keep their enviroment" )
else:
        print("great i hope you abright future")
print(score + 10)

# question 3
question_3 = print(input("what is your favorate color ?"))
if question_3 == color_1:
        print(color_1,"it good for your computer theme ")
elif question_3 == color_2:
        print(color_2,"i dont prefere this color becouse it is the color blood")
else:
        print("colors are generaly from three colors red green and blue")
print(score + 10)
