
name = input("Enter your name: ")
print("Welcome", name)

score = 0

# Q1
print("1. What is used to display output?")
if input("Your answer: ").lower() == "print":
    print("Correct"); score += 1
else: print("Wrong")

# Q2
print("2. What is used to take input?")
if input("Your answer: ").lower() == "input":
    print("Correct"); score += 1
else: print("Wrong")

# Q3
print("3. What type is 'Hello'?")
if input("Your answer: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q4
print("4. What type is 10?")
if input("Your answer: ").lower() == "int":
    print("Correct"); score += 1
else: print("Wrong")

# Q5
print("5. What type is 3.5?")
if input("Your answer: ").lower() == "float":
    print("Correct"); score += 1
else: print("Wrong")

# Q6
print("6. What type is True?")
if input("Your answer: ").lower() == "boolean":
    print("Correct"); score += 1
else: print("Wrong")

# Q7
print("7. What symbol is used for comments?")
if input("Your answer: ") == "#":
    print("Correct"); score += 1
else: print("Wrong")

# Q8
print("8. What does == mean?")
if "equal" in input("Your answer: ").lower():
    print("Correct"); score += 1
else: print("Wrong")

# Q9
print("9. What does = mean?")
if "assign" in input("Your answer: ").lower():
    print("Correct"); score += 1
else: print("Wrong")

# Q10
print("10. What is printed: print('Hi')?")
if input("Your answer: ").lower() == "hi":
    print("Correct"); score += 1
else: print("Wrong")

# Q11
print("11. What type is '5'?")
if input("Your answer: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q12
print("12. What type is False?")
if input("Your answer: ").lower() == "boolean":
    print("Correct"); score += 1
else: print("Wrong")

# Q13
print("13. Is Python case sensitive? (yes/no)")
ans = input("Your answer: ").lower()
if ans == "yes" or ans == "y":
    print("Correct"); score += 1
else: print("Wrong")

# Q14
print("14. 'A' == 'A'? (true/false)")
if input("Your answer: ").lower() == "true":
    print("Correct"); score += 1
else: print("Wrong")

# Q15
print("15. 'A' == 'a'? (true/false)")
if input("Your answer: ").lower() == "false":
    print("Correct"); score += 1
else: print("Wrong")

# Q16
print("16. What symbol assigns value?")
if input("Your answer: ") == "=":
    print("Correct"); score += 1
else: print("Wrong")

# Q17
print("17. What keyword starts a condition?")
if input("Your answer: ").lower() == "if":
    print("Correct"); score += 1
else: print("Wrong")

# Q18
print("18. What keyword is used for another condition?")
if input("Your answer: ").lower() == "else":
    print("Correct"); score += 1
else: print("Wrong")

# Q19
print("19. What keyword checks another condition?")
if input("Your answer: ").lower() == "elif":
    print("Correct"); score += 1
else: print("Wrong")

# Q20
print("20. What does input() return?")
if input("Your answer: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q21
print("21. What will print: print(1 == 1)?")
if input("Your answer: ").lower() == "true":
    print("Correct"); score += 1
else: print("Wrong")

# Q22
print("22. What will print: print(1 == 2)?")
if input("Your answer: ").lower() == "false":
    print("Correct"); score += 1
else: print("Wrong")

# Q23
print("23. What type is 0.0?")
if input("Your answer: ").lower() == "float":
    print("Correct"); score += 1
else: print("Wrong")

# Q24
print("24. What type is 0?")
if input("Your answer: ").lower() == "int":
    print("Correct"); score += 1
else: print("Wrong")

# Q25
print("25. What will print: print('A' + 'B')?")
if input("Your answer: ").lower() == "ab":
    print("Correct"); score += 1
else: print("Wrong")

# Q26
print("26. What will print: print('Hi' * 2)?")
if input("Your answer: ").lower() == "hihi":
    print("Correct"); score += 1
else: print("Wrong")

# Q27
print("27. Is 5 == '5'? (true/false)")
if input("Your answer: ").lower() == "false":
    print("Correct"); score += 1
else: print("Wrong")

# Q28
print("28. What is the result type of input()?")
if input("Your answer: ").lower() == "string":
    print("Correct"); score += 1
else: print("Wrong")

# Q29
print("29. What keyword is used to write a condition?")
if input("Your answer: ").lower() == "if":
    print("Correct"); score += 1
else: print("Wrong")

# Q30
print("30. What will print: print(True)?")
if input("Your answer: ").lower() == "true":
    print("Correct"); score += 1
else: print("Wrong")

print(name, "your score is", score, "out of 30")