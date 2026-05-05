
## Assignment 1: Temperature from the user

# Write `temperature_input.py` that:

# 1. Asks the user for a **temperature** as an integer (use `input()` and `int(...)`).
# 2. Uses **`if` / `elif` / `else`** with the **same thresholds** as the `if-elif-else` lesson mini practice: **25 or above** → print `"warm"`; **15 or above** (but below 25) → print `"ok"`; otherwise → print `"cold"`.

# **Deliverable:** `temperature_input.py` + one example run pasted (any integer you type is fine).

input_temperature = int(input("Enter a temperature: "))
if input_temperature >= 25:
    print("warm")
elif input_temperature >= 15:
    print("ok")
else:
    print("cold")
