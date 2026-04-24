# Abdifatah mursal mohamed
# This is a simple quiz program that asks the user five question

user_name = input("magacaaga soo geli: ")
print("Welcome, ", user_name)

# inta variables aan isticmaali rabo
score = 0
total_questions = 5

# su'aasha 1
print("maxaa laga soo gaabiyey AI?")
jawaab = input("jawaabtu waa: ")

if jawaab == "Artificial Intelligence" or jawaab == "Garaad Gacmeed":
    print("sax! AI waxaa laga soo gaabiyey Artificial Intelligence ama Garaad Gacmeed .")
    score += 1
else:
    print("Qalad. AI waxaa laga soo gaabiyey Artificial Intelligence ama Garaad Gacmeed")

# su'aasha  2
print("Sanadkii ugu horeysay ay la soo daayey python waa? ")
jawaab = input("jawaabtu waa: ") 

if jawaab == "Waa sanadkii 1991" :
    print("sax! waxaa la soo daayey sanadkii 1991.")
    score += 1
else:
    print("Qalad. waxaa la soo daayey sanadkii 1991.")

# su'aasha  3
print("waxaad sheegtaa meelaha qaar oo loo adeegsankaro luqada python?  ") 
jawaab = input("jawaabtu waa: ") 

if jawaab == "ALI iyo ML " or jawaab == "Web development iyo Data science":
    print("sax! waxaa loo adeegsankaraa meelahan ay kamid tahay ALI iyo ML,Web development iyo Data science")
    score += 1
else:    
    print("Qalad. waxaa loo adeegsankaraa meelahan ay kamid tahay ALI iyo ML,Web development iyo Data science")
# su'aasha 4
print("python for everyone Bootcamp yaa taabagelinaya?")
jawaab = input("jawaabtu waa:  ")
if jawaab == ("Dugsiiye"):
    print("sax! waxaa taabagalinaya dugsiiye")
    score +=1
else:
    print("Qalad. waxaa taabagalinaya dugsiiye")
#su'aasha 5
print("dugsiiye maxay qabataa?")
jawaab = input("jawaabtu waa:  ")
if jawaab == ("dugsiiye waa madal lagu barto technology ay kamid yihiin software engineering iyo AI"):
    print("sax!. dugsiiye waa madal lagu barto technology ay kamid yihiin software engineering iyo AI")
    score +=1
else:
    print("Qalad.dugsiiye waa madal lagu barto technology ay kamid yihiin software engineering iyo AI")
print(user_name, "You've scored ", score, " out of", total_questions)