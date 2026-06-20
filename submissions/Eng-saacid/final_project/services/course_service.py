from utils.helpers import generate_id
from utils.storage import load_data, save_data
from services.teacher_service import TeacherService


class CourseService:

    def add_course(self, course: dict) -> None:

        data = load_data()

        data.setdefault("courses", []).append(course)

        save_data(data)

    def get_courses(self) -> list:

        data = load_data()

        return data.get("courses", [])

    def find_course(self, course_id: str) -> dict | None:

        course_id = course_id.strip().upper()
        data = load_data()

        for course in data.get("courses", []):

            if course["id"] == course_id:
                return course

        return None

    def update_course(
        self,
        course_id: str,
        title: str | None = None,
        duration: str | None = None,
        teacher_id: str | None = None
    ) -> bool:

        course_id = course_id.strip().upper()
        data = load_data()

        for course in data.get("courses", []):

            if course["id"] == course_id:

                if title is not None:
                    course["title"] = title

                if duration is not None:
                    course["duration"] = duration

                if teacher_id is not None:
                    course["teacher_id"] = teacher_id

                save_data(data)

                return True

        return False

    def delete_course(self, course_id: str) -> bool:

        course_id = course_id.strip().upper()
        data = load_data()

        courses = data.get("courses", [])

        for course in courses:

            if course["id"] == course_id:

                courses.remove(course)

                save_data(data)

                return True

        return False


def course_menu():

    course_service = CourseService()
    teacher_service = TeacherService()

    while True:

        print("""
--- Course Menu ---

1. Add Course
2. View Courses
3. Search Course
4. Update Course
5. Delete Course
6. Back
0. Exit
""")

        choice = input("Choose: ").strip()

        # Add Course
        if choice == "1":

            title = input("Enter course title: ").strip()
            duration = input("Enter course duration: ").strip()
            teacher_id = input("Enter Teacher ID: ").strip().upper()

            teacher = teacher_service.find_teacher(
                teacher_id
            )

            if not teacher:
                print("Teacher not found")
                continue

            data = load_data()

            course = {
                "id": generate_id(data.get("courses", []), "CR"),
                "title": title,
                "duration": duration,
                "teacher_id": teacher_id
            }

            course_service.add_course(course)

            print("Course added successfully")

        # View Courses
        elif choice == "2":

            courses = course_service.get_courses()

            if not courses:
                print("No courses found.")
                continue

            print("\n===== COURSES LIST =====")

            for course in courses:
                teacher = teacher_service.find_teacher(
                    course["teacher_id"]
                )

                teacher_name = (
                    teacher["name"]
                    if teacher
                    else "Unknown"
                )

                print(
                    f"> ID: {course['id']}, "
                    f"Title: {course['title']}, "
                    f"Duration: {course['duration']}"
                    f", Teacher: {teacher_name}"
                )

        # Search Course
        elif choice == "3":

            course_id = input("Enter course ID: ").strip().upper()

            course = course_service.find_course(course_id)

            if course:

                print(
                    f"> ID: {course['id']}, "
                    f"Title: {course['title']}, "
                    f"Duration: {course['duration']}"
                )

            else:
                print("Course not found")

        # Update Course
        elif choice == "4":

            course_id = input("Enter course ID: ").strip().upper()

            title = input("Enter new title: ").strip()
            duration = input("Enter new duration: ").strip()
            teacher_id = input("Enter new teacher ID: ").strip().upper()

            title = title if title else None
            duration = duration if duration else None
            teacher_id = teacher_id if teacher_id else None

            if course_service.update_course(
                course_id,
                title,
                duration,
                teacher_id
            ):
                print("Course updated successfully")

            else:
                print("Course not found")

        # Delete Course
        elif choice == "5":

            course_id = input("Enter course ID: ").strip().upper()

            if course_service.delete_course(course_id):
                print("Course deleted successfully")

            else:
                print("Course not found")

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
            print("Invalid choice")
