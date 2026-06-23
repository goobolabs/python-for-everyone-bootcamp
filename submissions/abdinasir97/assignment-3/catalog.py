# prepared by abdinasir97
# personal catalog

# str and int
geeting = "how are you"
year = 2026
print(geeting)

    # class for clothes
class cloths:
    def __init__(self, shirt,T_shirt,shoes,eye_glassess):
        self.shirt = shirt
        self.T_shirt = T_shirt
        self.shoes = shoes
        self.eyeglasess = eye_glassess
    
dress = cloths("white_shirt","sports_T_shirt","black_shoes","protector eye_glassess")
print(dress.shoes)

# using try and except reading file
try:
    with open("abdinasir.txt" "r",encoding="UTF=8") as file:
        content = file.read
        print(content)
except FileNotFoundError:
    print("this file not found please check")
    
# writing file
with open("abdinasir.txt","w", encoding="utf-8") as file:
    file.write("hello wold this is python course itsnot easy")
    print(file)
# using while loop
name = ""
while name != "abdinasir":
    name = input("what is your name ?")
    if name != "abdinasir":
        print("you are not abdinasir")
print("well come ",name)