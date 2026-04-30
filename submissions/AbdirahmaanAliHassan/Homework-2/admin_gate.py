# Assignment 2: Nested questions (admin gate)
# 1. Asks for a username with input().
username = "admin"
password = "secret"

name = input("Enter your username: ")

# 2. If the username is "admin", asks for a password. If the password is "secret", prints "Access granted". Otherwise prints "Wrong password".

if name == username:
    EnterPassword = input("Enter Your Password: ")
    if EnterPassword == password:
        print("access grant: ")
    else:
        print("Wrong password")


# 3. If the username is not admin, prints "Unknown user" and does not ask for a password.

if name != "admin":
    print("Unknown User")



    # code-ka 3-da Homework

# username = "admin"
# password = "secret"

# name = input("Enter your username: ")

# if name == username:
#     EnterPassword = input("Enter your password: ")
    
#     if EnterPassword == password:
#         print("Access granted")
#     else:
#         print("Wrong password")
# else:
#     print("Unknown user")