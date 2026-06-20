from services.course_service import CourseService
from utils.helpers import generate_id
from utils.storage import load_data, save_data


class StudentService:

    def add_student(self, student: dict) -> None:
        data = load_data()

        data.setdefault("students", []).append(student)

        save_data(data)

    def get_students(self) -> list:
        data = load_data()

        return data.get("students", [])

    def find_student(self, student_id: str) -> dict | None:
        student_id = student_id.strip().upper()
        data = load_data()

        for student in data.get("students", []):

            if student["id"] == student_id:
                return student

        return None

    def delete_student(self, student_id: str) -> bool:
        student_id = student_id.strip().upper()
        data = load_data()

        students = data.get("students", [])

        for student in students:

            if student["id"] == student_id:

                students.remove(student)

                save_data(data)

                return True

        return False

    def update_student(
        self,
        student_id: str,
        name: str | None = None,
        age: int | None = None
    ) -> bool:
        student_id = student_id.strip().upper()
        data = load_data()

        for student in data.get("students", []):

            if student["id"] == student_id:

                if name is not None:
                    student["name"] = name

                if age is not None:
                    student["age"] = age

                save_data(data)

                return True

        return False

    def enroll_student_in_course(
        self,
        student_id: str,
        course_id: str
    ) -> bool:

        student_id = student_id.strip().upper()
        course_id = course_id.strip().upper()
        data = load_data()

        for student in data.get("students", []):

            if student["id"] == student_id:

                enrolled_courses = student.setdefault(
                    "enrolled_courses",
                    []
                )

                if course_id not in enrolled_courses:

                    enrolled_courses.append(course_id)

                    save_data(data)

                    return True

                print(
                    f"{student['name']} already enrolled "
                    f"in course {course_id}"
                )

                return False

        return False

    def unenroll_student_from_course(
        self,
        student_id: str,
        course_id: str
    ) -> bool:

        student_id = student_id.strip().upper()
        course_id = course_id.strip().upper()
        data = load_data()

        for student in data.get("students", []):

            if student["id"] == student_id:

                enrolled_courses = student.get(
                    "enrolled_courses",
                    []
                )

                if course_id in enrolled_courses:

                    enrolled_courses.remove(course_id)

                    save_data(data)

                    return True

                print(
                    f"{student['name']} is not enrolled "
                    f"in course {course_id}"
                )

                return False

        return False


def student_menu():

    student_service = StudentService()
    while True:
        print("""
--- Student Menu ---

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Back 
0. Exit
            """)
        choice = input("Choose: ").strip()
        if choice == "1":

            name = input("Enter name: ").strip()
            age = input("Enter age: ").strip()
            data = load_data()
            student = {
                "id": generate_id(data.get("students", []), "ST"),
                "name": name,
                "age": age
            }

            student_service.add_student(student)

            print("Student added successfully")

        elif choice == "2":

            students = student_service.get_students()

            if not students:
                print("No students found.")
                continue

            print("\n===== STUDENTS LIST =====")
            for student in students:
                print(
                    f"> ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
        elif choice == "3":
            student_id = input("Enter student ID: ").strip().upper()

            student = student_service.find_student(student_id)

            if student:
                print(
                    f"> ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
            else:
                print("Student not found")
        elif choice == "4":
            student_id = input("Enter student ID: ").strip().upper()

            name = input("Enter new name: ").strip()
            age = input("Enter new age : ").strip()

            name = name if name else None
            age = int(age) if age else None

            if student_service.update_student(student_id, name, age):
                print("Student updated successfully")
            else:
                print("Student not found")
        elif choice == "5":
            student_id = input("Enter student ID: ").strip().upper()

            if student_service.delete_student(student_id):
                print("Student deleted successfully")
            else:
                print("Student not found")
        elif choice == "6":
            save_data(load_data())  # Ensure data is saved before going back
            break
        elif choice == "0":
            save_data(load_data())
            # Ensure data is saved before exiting
            print("\nExiting program...\n")
            exit()


def enrollment_menu():

    student_service = StudentService()

    while True:

        print("""
--- Enrollment Menu ---

1. Enroll Student in Course
2. Unenroll Student from Course
3. View Student Courses
4. Back
0. Exit
""")

        choice = input("Choose: ").strip()

        # Enroll
        if choice == "1":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            course_id = input(
                "Enter Course ID: "
            ).strip().upper()

            course = CourseService().find_course(course_id)

            if not course:
                print("Course not found")
                continue

            if student_service.enroll_student_in_course(
                student_id,
                course_id
            ):
                print("Student enrolled successfully")
            else:
                print("Enrollment failed")

        # Unenroll
        elif choice == "2":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            course_id = input(
                "Enter Course ID: "
            ).strip().upper()

            if student_service.unenroll_student_from_course(
                student_id,
                course_id
            ):

                print(
                    "Student removed from course"
                )

            else:

                print(
                    "Operation failed"
                )

        # View Courses
        elif choice == "3":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            student = student_service.find_student(
                student_id
            )

            if student:

                courses = student.get(
                    "enrolled_courses",
                    []
                )

                if courses:

                    print(
                        f"\nCourses for {student['name']}:"
                    )

                    for course_id in courses:

                        course = CourseService().find_course(course_id)

                        if course:
                            print(
                                f"{course['id']} - {course['title']}"
                            )
                else:
                    print("No enrolled courses")

            else:

                print(
                    "Student not found"
                )

        # Back
        elif choice == "4":
            break

        # Exit
        elif choice == "0":

            print(
                "\nExiting program...\n"
            )

            exit()

        else:

            print(
                "Invalid choice"
            )
