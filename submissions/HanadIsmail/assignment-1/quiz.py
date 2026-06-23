name = input("What is your name: ")
print("Welcome,", name)

score = 0
questions = 3

# Question 1
print("Waa kuma Ra'iisul Wasaaraha Somalia?")
ans = input("Jawaabta: ").lower().strip()

# accepts: hamze abdi or xamze cabdi
if ans == "hamze abdi" or ans == "xamze cabdi":
    print("Sax ✅")
    score = score + 1
else:
    print("Qalad ❌")

# Question 2
print("Waa maxay caasimada Somalia?")
ans = input("Jawaabta: ").lower().strip()

if ans == "mogadishu" or ans == "muqdisho":
    print("Sax ✅")
    score = score + 1
else:
    print("Qalad ❌")

# Question 3
print("Somalia qaaradee ayay ku taalaa?")
ans = input("Jawaabta: ").lower().strip()

if ans == "africa" or ans == "afrika":
    print("Sax ✅")
    score = score + 1
else:
    print("Qalad ❌")

print("Waxaad saxday:", score, "/", questions)