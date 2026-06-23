from pathlib import Path

from models.students import School, Student

# Default data file lives under project_folder/data/
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "students.txt"

# First data row acts as column labels (readable in spreadsheets as "pipe-separated").
FILE_HEADER = "id|name|grades"


def parse_grades(s: str) -> list[float]:
    s = s.strip()
    if not s:
        return []
    return [float(p.strip()) for p in s.split(",") if p.strip()]


def _is_column_header_line(line: str) -> bool:
    """Skip the readable column row (matches id|name|grades, any column spacing)."""
    return line.strip().lower().replace(" ", "") == FILE_HEADER.lower().replace(" ", "")


def load_school(path: Path, school: School) -> None:
    school.clear()
    try:
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if _is_column_header_line(line):
                    continue
                parts = line.split("|", 2)
                if len(parts) != 3:
                    continue
                sid, name, grades_txt = parts[0].strip(), parts[1].strip(), parts[2]
                try:
                    grades = parse_grades(grades_txt)
                except ValueError:
                    continue
                school.add(Student(student_id=sid, name=name, grades=grades))
    except FileNotFoundError:
        pass


def save_school(path: Path, school: School) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Columns: pipe-separated rows after the header line.\n", f"{FILE_HEADER}\n"]
    for s in school.all():
        grades_txt = ",".join(str(g) for g in s.grades)
        lines.append(f"{s.student_id}|{s.name}|{grades_txt}\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
