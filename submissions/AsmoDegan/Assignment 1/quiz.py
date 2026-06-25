# Magaca: Asmo Abdulaahi
# Assegment 1: Barnaamij kedis ah oo su'aalo weydiinaya qofka.

magaca = input("Fadlan magacaaga qor: ")
print("Ku soo dhowow kediska aduunka, " + magaca + "!")

dhibcaha = 0

# Su'aasha kowaad
print("\n1. Waa maxay caasimadda dalka Soomaaliya?")
jawaab1 = input("Jawaabtaada: ")

if jawaab1.lower() == "muqdisho" or jawaab1.lower() == "mogadishu":
    print("Sax! Waad ku dhuftay.")
    dhibcaha = dhibcaha + 1
else:
    print("Khalad, caasimaddu waa Muqdisho.")

# Su'aasha labaad 
print("\n2. Sheeg midabada uu ka koobanyahay calanka Jabuuti?")
print("(Talo: Kala saar midabada adoo isticmaalaya space)")
jawaab2 = input("Jawaabtaada: ").lower()

# Waxaan eegaynaa haddii uu qofku wada sheegay midabada muhiimka ah
if "bulug" in jawaab2 and "cagar" in jawaab2 and "cadan" in jawaab2:
    print("Aad baad u mahadsantahay! Dhammaan midabada waad wada heshay.")
    dhibcaha += 1
else:
    print("Ma wada helin dhamaan midabada. Calanka Jabuuti waa bulug cagar iyo cadan")

# Su'aasha saddexaad
print("\n3. Dalka Itoobiya ma leeyahay bad (Haa ama Maya)?")
jawaab3 = input("Jawaabtaada: ")

if jawaab3.lower() == "maya":
    print("Waa sax, Itoobiya bad ma lahan.")
    dhibcaha += 1
else:
    print("Maya, jawaabtu waa maya.")

# Natiijada guud
print("\n--------------------")
print(magaca + ", kediskii wuu dhamaaday.")
print("Dhibcaha aad keentay waa: " + str(dhibcaha) + " oo ka mid ah 3.")
print("Mahadsanid!")
