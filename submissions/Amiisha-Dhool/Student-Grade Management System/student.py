class Student:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender

        # Subjects
        self.math = 0
        self.english = 0
        self.science = 0
        self.programming = 0

        # Results
        self.average = 0
        self.grade = "N/A"

    def calculate_average(self):
        self.average = (
            self.math +
            self.english +
            self.science +
            self.programming
        ) / 4
        return self.average

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = "A+"
        elif self.average >= 80:
            self.grade = "A"
        elif self.average >= 70:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

        return self.grade

    def display(self):
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Math       : {self.math}")
        print(f"English    : {self.english}")
        print(f"Science    : {self.science}")
        print(f"Programming: {self.programming}")
        print(f"Average    : {self.average:.2f}")
        print(f"Grade      : {self.grade}")
        print("-" * 40)

    # ✅ SAVE (object → dict)
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "math": self.math,
            "english": self.english,
            "science": self.science,
            "programming": self.programming,
            "average": self.average,
            "grade": self.grade
        }

    # ✅ LOAD (dict → object)
    @classmethod
    def from_dict(cls, data):
        student = cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["gender"]
        )

        student.math = data.get("math", 0)
        student.english = data.get("english", 0)
        student.science = data.get("science", 0)
        student.programming = data.get("programming", 0)
        student.average = data.get("average", 0)
        student.grade = data.get("grade", "N/A")

        return student