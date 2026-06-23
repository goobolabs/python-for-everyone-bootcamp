
name = input("what is your name? ")
print(f"welcome to the quiz {name}")
score = 0
question1 = input("wa kee programinka ugu fiican ee rabtid ina baratid? ")
question2 = input("waa maxay hadafkaaga ugu wayn aad leedahay  ")
question3 = input(
    "ma is leedahay waad niyad jabin mise waad dhamasan bootcamp ")
if question1 == "python":
    score += 1
if question2 == "ina data analysis baro":
    score += 1
if question3 == "my  ma niyad jabi doono":
    score += 1
print(f"{name} your score is {score}")
