

from services.course_service import course_menu
from services.grade_service import grade_menu
from services.student_service import enrollment_menu, student_menu
from services.teacher_service import teacher_menu
from services.users_service import UserService

# TODO: Admin Dashboard


def admin_menu(user):

    while True:

        print("""
===== ADMIN MENU =====

1. Students
2. Teachers
3. Courses
4. Enrollment
5. Grades
6. users
7. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_menu()

        elif choice == "2":
            teacher_menu()

        elif choice == "3":
            course_menu()

        elif choice == "4":
            enrollment_menu()

        elif choice == "5":
            grade_menu()

        elif choice == "6":
            user_menu()

        elif choice == "7":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue

# TODO: Teacher Dashboard


def teacher_dashboard(user):

    while True:

        print("""
===== TEACHER MENU =====

1. View Students
2. View Courses
3. Add Grades
4. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_menu()

        elif choice == "2":
            course_menu()

        elif choice == "3":
            grade_menu()

        elif choice == "4":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue

# TODO: Student Dashboard


def student_dashboard(user):

    while True:

        print("""
===== STUDENT MENU =====

1. View Courses
2. View Grades
3. Logout
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            course_menu()

        elif choice == "2":
            grade_menu()

        elif choice == "3":
            print("Logging out...")
            back_to_login = input("Go back to login? (y/n): ").strip().lower()
            if back_to_login == "y":
                print("Exiting...")
                break
            else:
                continue


# =========================
#       USER MENU
# =========================

def user_menu():

    service = UserService()

    while True:

        print("""
===== USER MANAGEMENT =====

1. Register User
2. View Users
3. Search User
4. Update User
5. Delete User
6. Back
0. Exit
""")

        choice = input(
            "Choose: "
        ).strip()

        # REGISTER USER
        if choice == "1":

            username = input(
                "Username: "
            ).strip()

            password = input(
                "Password: "
            ).strip()

            print("""
1. Admin
2. Teacher
3. Student
""")

            role_choice = input(
                "Choose Role: "
            ).strip()

            role = "student"

            if role_choice == "1":
                role = "admin"

            elif role_choice == "2":
                role = "teacher"

            service.register_user(
                username,
                password,
                role
            )

        # VIEW USERS
        elif choice == "2":

            users = service.get_users()

            if not users:

                print(
                    "No users found"
                )

                continue

            print(
                "\n===== USERS LIST ====="
            )

            for index, user in enumerate(
                users,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{user['username']} | "
                    f"{user['role']}"
                )

        # SEARCH USER
        elif choice == "3":

            username = input(
                "Enter Username: "
            ).strip()

            user = service.find_user(
                username
            )

            if user:

                print(
                    f"""
ID: {user['id']}
Username: {user['username']}
Role: {user['role']}
"""
                )

            else:

                print(
                    "User not found"
                )

        # UPDATE USER
        elif choice == "4":

            username = input(
                "Enter Username: "
            ).strip()

            user = service.find_user(
                username
            )

            if not user:

                print(
                    "User not found"
                )

                continue

            new_password = input(
                "New Password: "
            ).strip()

            print("""
1. Admin
2. Teacher
3. Student
""")

            role_choice = input(
                "Choose New Role: "
            ).strip()

            new_role = "student"

            if role_choice == "1":
                new_role = "admin"

            elif role_choice == "2":
                new_role = "teacher"

            if service.update_user(
                username,
                new_password,
                new_role
            ):

                print(
                    "User updated successfully"
                )

            else:

                print(
                    "Update failed"
                )

        # DELETE USER
        elif choice == "5":

            username = input(
                "Enter Username: "
            ).strip()

            if service.delete_user(
                username
            ):

                print(
                    "User deleted successfully"
                )

            else:

                print(
                    "User not found"
                )

        # BACK
        elif choice == "6":

            break

        # EXIT
        elif choice == "0":

            print(
                "Exiting..."
            )

            exit()

        else:

            print(
                "Invalid choice"
            )
