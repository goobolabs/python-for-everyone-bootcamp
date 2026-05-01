# galinta magaca iyo jawaabaha suaalaha
name = input("qor magacaaga? ")
print(f"kusoo dhowoow, {name}")
# suaasha 1
score = 0
answer = input("maxaad ka ka aaminsantahey python? ")
if answer == "luqad fudud":
    print(" waad saxantahey")
    score += 1
elif answer == "luqad adag":
    print("ma adka python")
    score += 1
else:
    print(" waad isku daydey mahadsanid")

# suaasha 2
answer = input("python goormee la sameeyey?")
if answer == "1991":
    print("waad saxantahey")
    score += 1
elif answer == "1998":
    print("lama sameynin 1998")
else:
    print("waad isku daydey mahadsanid")

# suaasha 3
answer = input("mala baran karaa python? ")
if answer == "haa":
    print("waad saxantahey")
    score += 1
elif answer == "maya":
    print("maya, waa la baran karaa")
else:
    print("waad isku daydey mahadsanid")

print(f" mahadsanid {name}, dhibcahada waa {score} out of 3.")
