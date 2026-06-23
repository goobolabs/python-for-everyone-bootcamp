"""Students in memory: the record (`Student`) and the group (`School`)."""

from dataclasses import dataclass, field


@dataclass
class Student:
    student_id: str
    name: str
    grades: list[float] = field(default_factory=list)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self) -> str:
        avg = self.average_grade()
        avg_txt = f"{avg:.2f}" if self.grades else "(no grades)"
        return f"{self.student_id} | {self.name} | grades={self.grades} | avg={avg_txt}"


class School:
    """Keeps everyone you know about — like `Catalog` in Assignment 3, but for pupils."""

    def __init__(self) -> None:
        self._students: list[Student] = []

    def add(self, student: Student) -> bool:
        if self.find_by_id(student.student_id) is not None:
            return False
        self._students.append(student)
        return True

    def remove(self, student_id: str) -> bool:
        sid = student_id.strip()
        for i, s in enumerate(self._students):
            if s.student_id == sid:
                del self._students[i]
                return True
        return False

    def find_by_id(self, student_id: str) -> Student | None:
        sid = student_id.strip()
        for s in self._students:
            if s.student_id == sid:
                return s
        return None

    def search(self, query: str) -> list[Student]:
        q = query.strip().lower()
        if not q:
            return []
        out: list[Student] = []
        for s in self._students:
            if q in s.student_id.lower() or q in s.name.lower():
                out.append(s)
        return out

    def all(self) -> list[Student]:
        return list(self._students)

    def update(
        self,
        student_id: str,
        *,
        name: str | None = None,
        grades: list[float] | None = None,
    ) -> bool:
        s = self.find_by_id(student_id)
        if s is None:
            return False
        if name is not None:
            s.name = name
        if grades is not None:
            s.grades = list(grades)
        return True

    def clear(self) -> None:
        self._students = []
