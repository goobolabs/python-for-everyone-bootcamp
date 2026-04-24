#===============================
# MAGACA: Python Basics Quiz
#===============================
Name=input("Enter your name:")
print("Welcom",Name)

result=0  # result waa mesha lagu kaydinayo jawaha
# question1 waa su aal string ah 
question1=input("Luuqaddee baa caan ku ah Data Science?")
if question1 == "Python":
    print("sax Python waa luqada uga caan san ee xogta loo is ticmaalo.")
    result += question1
else:
    print("Khalad! Jawaabtu waxay ahayd Python.")

# --- SU'AASHA 2AAD: Numeric Input & Math (Section 1 & 2)
print("waa maxay natijada soo baxayda (10/2)+5?")
Question2=float(input("Gali numberka saxda ah:"))
if Question2 == 10.0:
    print("Sax! Xisaabtu waa sax.")
    result += Question2
else:
        print("Khalad!Natiijadu waa 10.0.")
# --- SU'AASHA 3AAD: Trur or False
print("\n3. Ma run baa (True) mise waa been (False)?")
print("'Luuqadda Python waxaa la sameeyay 1991.'")
Question3 = input("Qor True ama False: ")

if Question3 == "True":
    print("Sax!Waa xaqiiqo taariikhi ah.")
    result += 1
else:
    print("Khalad! Waa run (True).")

# --- inta waxa aan ku xisabinaya resultiga guud  ---
print(f"DHAMAAD! {Name}, dhibcahaagu waa: {result}/3")

if result == 3:
    print("Darajo: Aad iyo aad u fiican!")
elif result >= 1:
    print("Darajo: Way fiican tahay, laakiin wax dadaal.")
else:
    print("Darajo: Isku day kale, dib u akhri casharka.")