from student import Student
from storage import load_students, save_students


def display_menu():
    print("\n" + "=" * 45)
    print("   STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Student Grades")
    print("7. Save Data")
    print("8. Exit")
    print("=" * 45)


def find_student(students, student_id):
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def main():
    students = load_students()

    while True:
        display_menu()
        choice = input("Enter choice (1-8): ").strip()
        print("You entered:", repr(choice))

        # 1. ADD
        if choice == "1":
            student_id = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")

            students.append(Student(student_id, name, age, gender))
            print("Student added!")

        # 2. VIEW
        elif choice == "2":
            print("\n--- ALL STUDENTS ---")

            if not students:
                print("No students found.")
            else:
                for s in students:
                    s.display()

        # 3. SEARCH
        elif choice == "3":
            sid = input("Enter ID: ")
            s = find_student(students, sid)

            if s:
                s.display()
            else:
                print("Student not found")

        # 4. UPDATE
        elif choice == "4":
            sid = input("Enter ID: ")
            s = find_student(students, sid)

            if s:
                s.name = input("New Name: ")
                s.age = int(input("New Age: "))
                s.gender = input("New Gender: ")
                print("Updated!")
            else:
                print("Not found")

        # 5. DELETE
        elif choice == "5":
            sid = input("Enter ID: ")
            s = find_student(students, sid)

            if s:
                students.remove(s)
                print("Deleted!")
            else:
                print("Not found")

        # 6. GRADES
        elif choice == "6":
            sid = input("Enter ID: ")
            s = find_student(students, sid)

            if s:
                subject = input("Subject: ")
                grade = float(input("Marks: "))

                setattr(s, subject, grade)

                s.calculate_average()
                s.calculate_grade()

                print("Grade added!")
            else:
                print("Student not found")

        # 7. SAVE
        elif choice == "7":
            try:
                print("Saving...")
                save_students(students)
                print("Saved successfully!")
            except Exception as e:
                print("Save error:", e)

        # 8. EXIT
        elif choice == "8":
            try:
                save_students(students)
            except:
                pass

            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()