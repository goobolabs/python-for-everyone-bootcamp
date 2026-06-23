
name = input("Gali magacaga: ")
print("Soo dhawow", name, "😊")

score = 0

# Su'aal 1
print("1. maxad u isticmaashaa si wax shaashadda ugu daabacdo?")
jawab = input("jawaab: ").lower()
if jawab == "print":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 2
print("2. maxay loo isticmaalaa si user ka input la qaato?")
jawab = input("jawaab: ").lower()
if jawab == "input":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 3
print("3. 'Hello' noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "string":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 4
print("4. 10 noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "int":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 5
print("5. 3.5 noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "float":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 6
print("6. True noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "boolean":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 7
print("7. comment-ka summaddiisu waa maxay?")
jawab = input("jawaab: ")
if jawab == "#":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 8
print("8. == macnahiisu waa maxay?")
jawab = input("jawaab: ").lower()
if "equal" in jawab:
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 9
print("9. = macnahiisu waa maxay?")
jawab = input("jawaab: ").lower()
if "assign" in jawab:
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 10
print("10. print('Hi') maxaa ka soo baxa?")
jawab = input("jawaab: ").lower()
if jawab == "hi":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 11
print("11. '5' noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "string":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 12
print("12. False noociisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "boolean":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 13
print("13. Python ma case-sensitive? (yes/no)")
jawab = input("jawaab: ").lower()
if jawab == "yes" or jawab == "y":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 14
print("14. 'A' == 'A' saxan? (true/false)")
jawab = input("jawaab: ").lower()
if jawab == "true":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 15
print("15. 'A' == 'a' saxan? (true/false)")
jawab = input("jawaab: ").lower()
if jawab == "false":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 16
print("16. value u xirta summaddeeda waa maxay?")
jawab = input("jawaab: ")
if jawab == "=":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 17
print("17. condition bilaaba keyword-kiisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "if":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 18
print("18. haddaan sax ahayn keyword-kiisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "else":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 19
print("19. condition kale hubinta keyword-kiisu waa maxay?")
jawab = input("jawaab: ").lower()
if jawab == "elif":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

# Su'aal 20
print("20. input() maxay soo celisaa?")
jawab = input("jawaab: ").lower()
if jawab == "string":
    score += 1
    print("Correct ✅")
else:
    print("Wrong ❌")

print("\n" + name + " score-kaagu waa", score, "/ 20")