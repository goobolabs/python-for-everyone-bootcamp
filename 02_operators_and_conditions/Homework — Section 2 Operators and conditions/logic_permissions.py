# ## Assignment 3: Logical combinations (`and` / `or`)

# Write `logic_permissions.py` that:

# 1. Asks the user for their **age** as an integer (`input()` and `int(...)`).
# 2. Asks whether a **parent or guardian is with them**, using a single letter answer: the user types **`y`** or **`n`** (compare the string to `"y"`).
# 3. Prints **`"OK to enter"`** if this rule is satisfied: **age is 13 or older**, **or** (**age is at least 10** **and** the parent answer is **`y`**). Otherwise prints **`"Sorry, not this time"`**.

# Use **`and`** and **`or`** in your condition (add **parentheses** so the rule is easy to read).

# **Deliverable:** `logic_permissions.py` + two example runs: one run that prints `"OK to enter"` and one that prints `"Sorry, not this time"`.

age = int(input("Enter your age: "))
parent_answer = input("Is a parent or guardian with you? (y/n): ")

if age >= 13 or (age >= 10 and parent_answer == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")
    