from utils.storage import load_data, save_data
# from services.grade_service import GradeService
from services.student_service import StudentService
from services.course_service import CourseService


# class GradeService:

#     def add_grade(self, grade: dict) -> bool:

#         data = load_data()

#         grades = data.setdefault("grades", [])

#         for g in grades:

#             if (
#                 g["student_id"] == grade["student_id"]
#                 and
#                 g["course_id"] == grade["course_id"]
#             ):
#                 return False

#         grades.append(grade)

#         save_data(data)

#         return True

#     def get_grades(self) -> list:

#         data = load_data()

#         return data.get("grades", [])

#     def find_grade(
#         self,
#         student_id: str,
#         course_id: str
#     ) -> dict | None:

#         student_id = student_id.strip().upper()
#         course_id = course_id.strip().upper()

#         data = load_data()

#         for grade in data.get("grades", []):

#             if (
#                 grade["student_id"] == student_id
#                 and
#                 grade["course_id"] == course_id
#             ):
#                 return grade

#         return None

#     def update_grade(
#         self,
#         student_id: str,
#         course_id: str,
#         new_grade: float
#     ) -> bool:

#         student_id = student_id.strip().upper()
#         course_id = course_id.strip().upper()

#         data = load_data()

#         for grade in data.get("grades", []):

#             if (
#                 grade["student_id"] == student_id
#                 and
#                 grade["course_id"] == course_id
#             ):

#                 grade["grade"] = new_grade

#                 save_data(data)

#                 return True

#         return False

#     def delete_grade(
#         self,
#         student_id: str,
#         course_id: str
#     ) -> bool:

#         student_id = student_id.strip().upper()
#         course_id = course_id.strip().upper()

#         data = load_data()

#         grades = data.get("grades", [])

#         for grade in grades:

#             if (
#                 grade["student_id"] == student_id
#                 and
#                 grade["course_id"] == course_id
#             ):

#                 grades.remove(grade)

#                 save_data(data)

#                 return True

#         return False
    
class GradeService:

    def add_grade(self, grade: dict) -> bool:

        data = load_data()
        grades = data.setdefault("grades", [])

        # VALIDATE grade value
        if not (0 <= grade["grade"] <= 100):
            print("Grade must be between 0 and 100")
            return False

        # CHECK DUPLICATE (student + course)
        for g in grades:
            if (
                g["student_id"] == grade["student_id"]
                and g["course_id"] == grade["course_id"]
            ):
                return False

        # ADD LETTER GRADE
        grade["letter"] = self.convert_grade(grade["grade"])

        grades.append(grade)
        save_data(data)

        return True

    def get_grades(self) -> list:

        data = load_data()
        return data.get("grades", [])

    def find_grade(self, student_id: str, course_id: str) -> dict | None:

        student_id = student_id.strip().upper()
        course_id = course_id.strip().upper()

        data = load_data()

        for grade in data.get("grades", []):

            if (
                grade["student_id"] == student_id
                and grade["course_id"] == course_id
            ):
                return grade

        return None

    def update_grade(self, student_id: str, course_id: str, new_grade: float) -> bool:

        student_id = student_id.strip().upper()
        course_id = course_id.strip().upper()

        data = load_data()

        if not (0 <= new_grade <= 100):
            print("Grade must be between 0 and 100")
            return False

        for grade in data.get("grades", []):

            if (
                grade["student_id"] == student_id
                and grade["course_id"] == course_id
            ):
                grade["grade"] = new_grade
                grade["letter"] = self.convert_grade(new_grade)

                save_data(data)
                return True

        print("Grade not found")
        return False

    def delete_grade(self, student_id: str, course_id: str) -> bool:

        student_id = student_id.strip().upper()
        course_id = course_id.strip().upper()

        data = load_data()
        grades = data.get("grades", [])

        for grade in grades:

            if (
                grade["student_id"] == student_id
                and grade["course_id"] == course_id
            ):
                grades.remove(grade)
                save_data(data)
                return True

        print("Grade not found")
        return False

    # 🔥 LETTER GRADE CONVERTER
    def convert_grade(self, score: float) -> str:

        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"


def grade_menu():

    grade_service = GradeService()
    student_service = StudentService()
    course_service = CourseService()

    while True:

        print("""
--- Grade Menu ---

1. Add Grade
2. View Grades
3. Search Grade
4. Update Grade
5. Delete Grade
6. Back
0. Exit
""")

        choice = input("Choose: ").strip()

        # Add Grade

        if choice == "1":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            course_id = input(
                "Enter Course ID: "
            ).strip().upper()

            # Check Student
            student = student_service.find_student(
                student_id
            )

            if not student:

                print(
                    "Student not found"
                )

                continue

            # Check Course
            course = course_service.find_course(
                course_id
            )

            if not course:

                print(
                    "Course not found"
                )

                break;

            # Check Enrollment
            if course_id not in student.get(
                "enrolled_courses",
                []
            ):

                print(
                    "Student is not enrolled in this course"
                )

                continue

            # Grade Input
            try:

                grade_value = float(
                    input(
                        "Enter Grade (0 - 100): "
                    )
                )

            except ValueError:

                print(
                    "Invalid grade"
                )

                continue

            # Grade Validation
            if grade_value < 0 or grade_value > 100:

                print(
                    "Grade must be between 0 and 100"
                )

                continue

            grade = {
                "student_id": student_id,
                "course_id": course_id,
                "grade": grade_value
            }

            if grade_service.add_grade(
                grade
            ):

                print(
                    "Grade added successfully"
                )

            else:

                print(
                    "Grade already exists for this student and course"
                )

        # View Grades
        # elif choice == "2":

        #     grades = grade_service.get_grades()

        #     if not grades:
        #         print("No grades found")
        #         continue

        #     print("\n===== GRADES LIST =====")

        #     for grade in grades:

        #         student = student_service.find_student(
        #             grade["student_id"]
        #         )

        #         course = course_service.find_course(
        #             grade["course_id"]
        #         )

        #         student_name = (
        #             student["name"]
        #             if student else
        #             "Unknown Student"
        #         )

        #         course_title = (
        #             course["title"]
        #             if course else
        #             "Unknown Course"
        #         )

        #         print(
        #             f"Student: {student_name} | "
        #             f"Course: {course_title} | "
        #             f"Grade: {grade['grade']}"
        #         )

        # VIEW
        elif choice == "2":

            grades = grade_service.get_grades()

            if not grades:
                print("No grades found")
                continue

            grouped = {}

            # GROUP BY STUDENT
            for g in grades:

                student_id = g["student_id"]

                if student_id not in grouped:
                    grouped[student_id] = []

                grouped[student_id].append(g)

            print("\n===== GRADES LIST =====")

            # DISPLAY
            for index, (student_id, student_grades) in enumerate(grouped.items(), start=1):

                student = student_service.find_student(student_id)

                student_name = (
                    student["name"]
                    if student else
                    "Unknown Student"
                )

                print(f"\n{index}.{student_name}")

                for g in student_grades:

                    course = course_service.find_course(
                        g["course_id"]
                    )

                    course_title = (
                        course["title"]
                        if course else
                        "Unknown Course"
                    )

                    print(
                        f"   {course_title} "
                        f"=> {g['grade']} "
                        f"({g['letter']})"
                    )

        # Search Grade
        # elif choice == "3":

        #     student_id = input(
        #         "Enter Student ID: "
        #     ).strip().upper()

        #     course_id = input(
        #         "Enter Course ID: "
        #     ).strip().upper()

        #     grade = grade_service.find_grade(
        #         student_id,
        #         course_id
        #     )

        #     if grade:

        #         student = student_service.find_student(
        #             student_id
        #         )

        #         course = course_service.find_course(
        #             course_id
        #         )
        #         print("\n===== GRADES LIST =====")
        #         print(
                    
        #             f"Student: {student['name']} | "
        #             f"Course: {course['title']} | "
        #             f"Grade: {grade['grade']} ({grade['letter']})"
        #         )

        #     else:

        #         print("Grade not found")

                # SEARCH STUDENT GRADES
        elif choice == "3":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            grades = grade_service.get_grades()

            student = student_service.find_student(
                student_id
            )

            if not student:
                print("Student not found")
                continue

            student_grades = []

            for g in grades:

                if g["student_id"] == student_id:
                    student_grades.append(g)

            if not student_grades:
                print("No grades found")
                continue

            print(f"\n===== {student['name']} GRADES =====")

            for g in student_grades:

                course = course_service.find_course(
                    g["course_id"]
                )

                course_title = (
                    course["title"]
                    if course else
                    "Unknown Course"
                )

                print(
                    f"{course_title} "
                    f"=> {g['grade']} "
                    f"({g['letter']})"
                )

        # Update Grade
        elif choice == "4":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            course_id = input(
                "Enter Course ID: "
            ).strip().upper()

            new_grade = float(
                input("Enter New Grade: ")
            )

            if grade_service.update_grade(
                student_id,
                course_id,
                new_grade
            ):

                print(
                    "Grade updated successfully"
                )

            else:

                print(
                    "Grade not found"
                )

        # Delete Grade
        elif choice == "5":

            student_id = input(
                "Enter Student ID: "
            ).strip().upper()

            course_id = input(
                "Enter Course ID: "
            ).strip().upper()

            if grade_service.delete_grade(
                student_id,
                course_id
            ):

                print(
                    "Grade deleted successfully"
                )

            else:

                print(
                    "Grade not found"
                )

        # Back
        elif choice == "6":

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