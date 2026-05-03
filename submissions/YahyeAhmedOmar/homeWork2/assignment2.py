# admin_gate.py

username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")