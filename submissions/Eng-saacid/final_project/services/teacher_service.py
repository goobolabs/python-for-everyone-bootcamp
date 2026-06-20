
from utils.helpers import generate_id
from utils.storage import load_data, save_data


# class TeacherService:

#     def add_teacher(self, teacher):

#         data = load_data()

#         data["teachers"].append(teacher)

#         save_data(data)

#     def get_teachers(self):

#         data = load_data()

#         return data["teachers"]

#     def find_teacher(self, teacher_id):

#         data = load_data()

#         for teacher in data["teachers"]:

#             if teacher["id"] == teacher_id:
#                 return teacher

#         return None

#     def update_teacher(
#             self,
#             teacher_id: str,
#             name: str | None = None,
#             subject: str | None = None
#     ):

#         data = load_data()

#         for teacher in data["teachers"]:

#             if teacher["id"] == teacher_id:

#                 if name is not None:
#                     teacher["name"] = name

#                 if subject is not None:
#                     teacher["subject"] = subject

#                 save_data(data)

#                 return True

#         return False

#     def delete_teacher(self, teacher_id):

#         data = load_data()

#         teachers = data["teachers"]

#         for teacher in teachers:

#             if teacher["id"] == teacher_id:

#                 teachers.remove(teacher)

#                 save_data(data)

#                 return True

#         return False

class TeacherService:

    def add_teacher(self, teacher: dict) -> None:
        data = load_data()

        data.setdefault("teachers", []).append(teacher)

        save_data(data)

    def get_teachers(self) -> list:
        data = load_data()

        return data.get("teachers", [])

    def find_teacher(self, teacher_id: str) -> dict | None:
        teacher_id = teacher_id.strip().upper()
        data = load_data()

        for teacher in data.get("teachers", []):

            if teacher["id"] == teacher_id:
                return teacher

        return None

    def delete_teacher(self, teacher_id: str) -> bool:
        teacher_id = teacher_id.strip().upper()
        data = load_data()

        teachers = data.get("teachers", [])

        for teacher in teachers:

            if teacher["id"] == teacher_id:

                teachers.remove(teacher)

                save_data(data)

                return True

        return False

    def update_teacher(
        self,
        teacher_id: str,
        name: str | None = None,
        subject: str | None = None
    ) -> bool:

        teacher_id = teacher_id.strip().upper()
        data = load_data()

        for teacher in data.get("teachers", []):

            if teacher["id"] == teacher_id:

                if name is not None:
                    teacher["name"] = name

                if subject is not None:
                    teacher["subject"] = subject

                save_data(data)

                return True

        return False

teacher_service = TeacherService()


def teacher_menu():

    while True:

        print("""
======== TEACHER MANAGEMENT ========

1. Add Teacher
2. View Teachers
3. Search Teacher
4. Update Teacher
5. Delete Teacher
6. Back
0. Exit

====================================
""")

        choice = input("Choose an option: ")

        # Add Teacher
        if choice == "1":

            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            data = load_data()
            teacher = {
                "id": generate_id(data.get("teachers", []), "TC"),
                "name": name,
                "subject": subject
            }

            teacher_service.add_teacher(teacher)

            print("\nTeacher added successfully!\n")

        # View Teachers
        elif choice == "2":

            teachers = teacher_service.get_teachers()

            if not teachers:
                print("\nNo teachers found.\n")

            else:

                print("\n===== TEACHERS LIST =====")

                for teacher in teachers:

                    print(
                        f"> ID: {teacher['id']}, Name: {teacher['name']}, Subject: {teacher['subject']}")

        # Search Teacher
        elif choice == "3":

            teacher_id = input("Enter Teacher ID: ").strip().upper()

            teacher = teacher_service.find_teacher(teacher_id)

            if teacher:

                print(
                    f"> ID: {teacher['id']}, Name: {teacher['name']}, Subject: {teacher['subject']}")

            else:
                print("\nTeacher not found.\n")

        # Update Teacher
        elif choice == "4":

            teacher_id = input("Enter Teacher ID: ").strip().upper()

            name = input("Enter new name: ").strip()
            subject = input("Enter new subject: ").strip()

            name= name if name else None
            subject = subject if subject else None

            if teacher_service.update_teacher(teacher_id, name, subject):
                print("\nTeacher updated successfully.\n")
            else:
                print("\nTeacher not found.\n")

        # Delete Teacher
        elif choice == "5":

            teacher_id = input("Enter Teacher ID: ").strip().upper()

            deleted = teacher_service.delete_teacher(teacher_id)

            if deleted:
                print("\nTeacher deleted successfully.\n")
            else:
                print("\nTeacher not found.\n")

        # Back
        elif choice == "6":
            save_data(load_data()) 
            break
        # Exit
        elif choice == "0":
            save_data(load_data()) 
            print("\nExiting program...\n")
            exit()

        else:
            print("\nInvalid choice. Try again.\n")
