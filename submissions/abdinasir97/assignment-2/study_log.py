# this is assignment two prepared by abdinasir97
#  02-study-log assigment

# part 1
name = input("what is your name ? ")
if name == "abdinasir":
        print("well come ",name)
elif name != "abdinasir":
        print("wrong name",name)
print(name)

# question one

question = input("which one is greater than abdi and ali ?" )
if question == "abdi":
     print("you are lying")
elif question == "ali":
    print(input("who told you ?"))
else:
    print(" i asked you abdi and ali only",question, "is your boket")
    
# question two
question2 = input("what is your title?")
if question2 =="engineer":
    print("good title mr",question2)
elif question2 =="doctor":
    print("good title but engineer is better than doctor")
else:
    print("please change your title ",question2, "into engineer")
    
    
# question three

stores = ["stoe_1","stoe_2", "stoe_3","stoe4"]
for c in stores:
    stores = input("which store do you work ?")
    if stores == "store4":
         print("well come boss")
    elif stores != "store4":
          print("wrong store number plz try again")
          
# questin four 

try:
    with open("note.txt","r", encoding="UTF-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("sorry the file is not available please re-cheack and try again ")
    
    
 if __name__ == "__main__":
    main()