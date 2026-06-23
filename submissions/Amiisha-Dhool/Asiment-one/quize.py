
name = input("gali magacaga: ")
print("soo dhawow", name)

score = 0

# Q1
print("1. maxad u isticmashay inputkaga ?")
if input(" jawabtada: ").lower() == "print":
    print("Correct"); score += 1
else: print("Wrong")

# Q2
print("2. What is used to take input?")
if input(" jawabtada: ").lower() == "input":
    print("Correct"); score += 1
else: print("Wrong")

# Q3
print("3. What type is 'Hello'?")
if input(" jawabtada: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q4
print("4. What type is 10?")
if input(" jawabtada: ").lower() == "int":
    print("Correct"); score += 1
else: print("Wrong")

# Q5
print("5. What type is 3.5?")
if input(" jawabtada: ").lower() == "float":
    print("Correct"); score += 1
else: print("Wrong")

# Q6
print("6. What type is True?")
if input(" jawabtada: ").lower() == "boolean":
    print("Correct"); score += 1
else: print("Wrong")

# Q7
print("7. What symbol is used for comments?")
if input(" jawabtada: ") == "#":
    print("Correct"); score += 1
else: print("Wrong")

# Q8
print("8. What does == mean?")
if "equal" in input(" jawabtada: ").lower(): 
    print("Correct"); score += 1
else: print("Wrong")

# Q9
print("9. What does = mean?")
if "assign" in input(" jawabtada: ").lower():
    print("Correct"); score += 1
else: print("Wrong")

# Q10
print("10. What is printed: print('Hi')?")
if input(" jawaabtada: ").lower() == "hi":
    print("Correct"); score += 1
else: print("Wrong")

# Q11
print("11. What type is '5'?")
if input(" jawaabtada: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q12
print("12. What type is False?")
if input(" jawaabtada: ").lower() == "boolean":
    print("Correct"); score += 1
else: print("Wrong")

# Q13
print("13. Is Python case sensitive? (yes/no)")
ans = input(" jawaabtada: ").lower()
if ans == "yes" or ans == "y":
    print("Correct"); score += 1
else: print("Wrong")

# Q14
print("14. 'A' == 'A'? (true/false)")
if input(" jawaabtada: ").lower() == "true":
    print("Correct"); score += 1
else: print("Wrong")

# Q15
print("15. 'A' == 'a'? (true/false)")
if input(" jawaabtada: ").lower() == "false":
    print("Correct"); score += 1
else: print("Wrong")

# Q16
print("16. What symbol assigns value?")
if input(" jawaabtada: ") == "=":
    print("Correct"); score += 1
else: print("Wrong")

# Q17
print("17. What keyword starts a condition?")
if input(" jawaabtada: ").lower() == "if":
    print("Correct"); score += 1
else: print("Wrong")

# Q18
print("18. What keyword is used for another condition?")
if input(" jawaabtada: ").lower() == "else":
    print("Correct"); score += 1
else: print("Wrong")

# Q19
print("19. What keyword checks another condition?")
if input(" jawaabtada: ").lower() == "elif":
    print("Correct"); score += 1
else: print("Wrong")

# Q20
print("20. What does input() return?")
if input(" jawaabtada: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

print(name, "your score is", score, "out of 20")




