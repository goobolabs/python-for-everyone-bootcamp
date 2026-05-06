
# my name is nasra
# i want to ask you some questions

name=(input("What Is Your Name ?"))
print("Welcome  :",name)
    
# su,aasha 1aad
Q1=int(input("Imisa Jus Ayuu Quran ku Ka kooban Yahay ?"))

natiijo=0
if  Q1==30:
    natiijo+=1
    print("Wad Garatay wll")
else :
    print("Wad qaladay wll soo dadaal")
# su,aasha 2aad
Q2=(input("miyad faraxsan thy: "))
if Q2=="haa" :
    natiijo+=1
    print("M.a Alle Hakuu Siyadiyo")
elif Q2=="maya" :
    print("Farxad badan ban ku rajeynaya")
# su,aasha 3aad
Q3=int(input("Quranka imisad jus bad ka taqaana"))
if Q3>=25 :
    natiijo+=1
    print("Wad Dadalaysa wll halkaas ka sii wad")
else :
    print("Si wacan ugu dadaal wll ")
# su,aasha 4aad
Q4=int(input("Waa maxay Isku Geyn ta laba Number ee kala ah 10 + 2  ?"))
if Q4==12 :
    natiijo+=1
    print("Wad Garatay wll")
else :
    print("Wad qaladay wll soo dadaal")

# su,aasha 5aad
Q5=int(input(" Imisa Wadan Bad taqaana Wll :"))
if Q5>=15:
    natiijo+=1
    print("OOV M.A wll Aqoon ba kaa buuxda")
else :
    print("Sidani Ma kaa dacad baa bal wax baro")

# natiijada ugu dambeysa mar walba soo baxda
print("waxad saxday",natiijo,"su,aalod  5 tii su,aalod")

    
