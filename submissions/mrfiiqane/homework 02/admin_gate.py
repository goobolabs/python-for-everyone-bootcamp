
# Assignment 2: Nested questions    admin gate

username = str(input("Enter username: "))

if username == "admin":
    password = int(input("Enter password: "))
    if password == 123:
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
