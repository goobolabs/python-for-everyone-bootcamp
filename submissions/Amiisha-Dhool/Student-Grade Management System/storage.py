import json
import os
from student import Student


FILE_NAME = "students.json"


def load_students():
    """Load students from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return [Student.from_dict(item) for item in data]

    except json.JSONDecodeError:
        print("⚠️ JSON file corrupted, resetting data...")
        return []

    except Exception as e:
        print("LOAD ERROR:", e)
        return []


def save_students(students):
    """Save students to JSON file safely."""

    try:
        data = []

        for student in students:
            data.append(student.to_dict())

        # 🔥 FIX: show real file location
        path = os.path.abspath(FILE_NAME)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)

        print("Saved here:", path)

    except Exception as e:
        print("SAVE ERROR:", e)