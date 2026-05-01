# Assignment 1: Temperature from the user
# 1. Asks the user for a temperature as an integer (use input() and int(...)).

temperature = int(input("Enter your temperature: "))
print(temperature)

# 2. Uses if / elif / else with the same thresholds as the if-elif-else lesson mini practice: 25 or above → print "warm"; 15 or above (but below 25) → print "ok"; otherwise → print "cold".

if temperature >= 25:
    print("warm")
elif 15 <= temperature < 25:
    print("ok")
else:
    print("cold")