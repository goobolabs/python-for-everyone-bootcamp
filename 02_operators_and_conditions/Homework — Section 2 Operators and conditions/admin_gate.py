# ## Assignment 2: Nested questions (admin gate)

# Write `admin_gate.py` that:

# 1. Asks for a **username** with `input()`.
# 2. If the username is **`"admin"`**, asks for a **password**. If the password is **`"secret"`**, prints **`"Access granted"`**. Otherwise prints **`"Wrong password"`**.
# 3. If the username is **not** `admin`, prints **`"Unknown user"`** and does **not** ask for a password.

# This matches the nested-conditions lesson mini practice, using the same strings.

# **Deliverable:** `admin_gate.py` + two example runs: one that reaches `"Access granted"`, and one that shows `"Unknown user"` or `"Wrong password"`.a


username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
