



from dataclasses import dataclass, field

@dataclass
class Student:
    id: int
    name: str
    enrolled_courses: list = field(default_factory=list)

    def enroll_course(self, course_id: int):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)
            print(f"Student {self.name} enrolled in course {course_id}.")
        else:
            print(f"Student {self.name} is already enrolled in course {course_id}.")
    def drop_course(self, course_id: int):
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)
            print(f"Student {self.name} dropped course {course_id}.")
        else:
            print(f"Student {self.name} is not enrolled in course {course_id}.")
    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', enrolled_courses={self.enrolled_courses})"
    
    