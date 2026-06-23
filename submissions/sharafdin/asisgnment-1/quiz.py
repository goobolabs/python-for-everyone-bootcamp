# Ask for user's name
name = input("Magacaaga geli: ")

print(f"Ku soo dhawoow, {name}!\n")

score = 0  # start from 0

# Question 1
q1 = input("Q1: 100 + 10 waa imisa? ")
if q1.strip() == "110":
    print("Sax!\n")
    score += 1
else:
    print("Qalad!\n")

# Question 2
q2 = input("Q2: 100 ÷ 5 waa imisa? ")
if q2.strip() == "20":
    print("Sax!\n")
    score += 1
else:
    print("Qalad!\n")

# Question 3
q3 = input("Q3: 100 × 8 waa imisa? ")
if q3.strip() == "800":
    print("Sax!\n")
    score += 1
else:
    print("Qalad!\n")

# Final score
print(f"{name}, waxaad saxday su`aalaha {score} out of 3.")Ali
