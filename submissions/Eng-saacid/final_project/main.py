from dashboards import admin_menu, admin_menu, student_dashboard, teacher_dashboard
from auth import Auth


auth = Auth()


def login_menu():

    print("\n===== LOGIN =====")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = auth.login(username, password)

    if not user:
        print("Invalid username or password")
        return login_menu()

    print(f"Welcome {user['username']} ({user['role']})")

    return user

def start_system():

    while True:

        user = login_menu()

        if not user:
            continue

        if user["role"] == "admin":
            admin_menu(user)

        elif user["role"] == "teacher":
            teacher_dashboard(user)

        elif user["role"] == "student":
            student_dashboard(user)


if __name__ == "__main__":
    start_system();