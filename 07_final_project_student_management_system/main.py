# Thin entry: menus and prompts. Domain in models/students.py; disk format in utils/storage.py.

from models.students import School, Student
from utils.storage import DATA_PATH, load_school, parse_grades, save_school


def menu_add(school: School) -> None:
    sid = input("Student id: ").strip()
    name = input("Name: ").strip()
    if not sid or not name:
        print("Id and name are required.")
        return
    line = input("Grades (comma-separated, optional): ").strip()
    try:
        grades = parse_grades(line)
    except ValueError:
        print("Grades must be numbers separated by commas (e.g. 88, 92).")
        return
    st = Student(student_id=sid, name=name, grades=grades)
    if school.add(st):
        print("Added.")
    else:
        print("That id already exists.")


def print_students(rows: list[Student]) -> None:
    if not rows:
        print("No students yet.")
        return
    for s in rows:
        print(f"  {s}")


def menu_list(school: School) -> None:
    print_students(school.all())


def menu_remove(school: School) -> None:
    sid = input("Student id to remove: ").strip()
    if school.remove(sid):
        print("Removed.")
    else:
        print("No student with that id.")


def menu_search(school: School) -> None:
    q = input("Search (id or part of name): ").strip()
    found = school.search(q)
    if not found:
        print("No matches.")
        return
    print_students(found)


def menu_update(school: School) -> None:
    sid = input("Student id to update: ").strip()
    if school.find_by_id(sid) is None:
        print("No student with that id.")
        return
    new_name = input("New name (Enter to keep): ").strip()
    raw = input(
        "New grades, comma-separated (Enter to keep; type none to clear): "
    ).strip()
    name_arg = new_name if new_name else None
    if raw.lower() == "none":
        grades_arg: list[float] | None = []
    elif raw:
        try:
            grades_arg = parse_grades(raw)
        except ValueError:
            print("Invalid grades; nothing changed.")
            return
    else:
        grades_arg = None
    if not school.update(sid, name=name_arg, grades=grades_arg):
        print("Update failed.")
        return
    print("Updated.")


def print_menu() -> None:
    print()
    print("--- Student management ---")
    print("1) Add student")
    print("2) List all")
    print("3) Remove student")
    print("4) Search")
    print("5) Update student")
    print("6) Save to file")
    print("0) Quit (also saves)")


def main() -> None:
    school = School()
    load_school(DATA_PATH, school)

    try:
        while True:
            print_menu()
            choice = input("Choice: ").strip()
            if choice == "1":
                menu_add(school)
            elif choice == "2":
                menu_list(school)
            elif choice == "3":
                menu_remove(school)
            elif choice == "4":
                menu_search(school)
            elif choice == "5":
                menu_update(school)
            elif choice == "6":
                save_school(DATA_PATH, school)
                print(f"Saved to {DATA_PATH}")
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Pick 0–6.")
    finally:
        try:
            save_school(DATA_PATH, school)
            print(f"Data saved to {DATA_PATH}")
        except OSError as e:
            print("Could not save:", e)


if __name__ == "__main__":
    main()
