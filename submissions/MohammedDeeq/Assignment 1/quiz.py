print("=== Quiz Fudud ===")

magac = input("Geli magacaaga: ")

dhibco = 0

print(f"\nKu soo dhowow {magac}, ka jawaab su'aalahan.\n")

j1 = input("1. Midabkee ayuu leeyahay calanka Soomaaliya? ")

if j1.strip().lower() in ["buluug", "buluug iyo caddaan"]:
    print("Jawaab sax ah!\n")
    dhibco += 1
else:
    print("Jawaab khaldan.\n")

j2 = input("2. Calaamaddee ayaa loo isticmaalaa comments-ka Python? ")

if j2.strip() == "#":
    print("Waad saxday!\n")
    dhibco += 1
else:
    print("Jawaab qaldan.\n")

j3 = input("3. Function-kee ayaa loo isticmaalaa in xog laga qaato user-ka? ")

if j3.lower() in ["input", "input()"]:
    print("Jawaab fiican!\n")
    dhibco += 1
else:
    print("Jawaab khaldan.\n")

print("===== Quiz-ka Waa Dhamaaday =====")
print(f"Magaca: {magac}")
print(f"Dhibcahaaga: {dhibco}/3")
