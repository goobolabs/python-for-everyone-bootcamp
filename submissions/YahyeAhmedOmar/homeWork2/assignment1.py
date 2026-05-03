# temperature_input.py

temperature = int(input("Enter temperature: "))

if temperature >= 25:
    print("warm")
elif temperature >= 15:
    print("ok")
else:
    print("cold")