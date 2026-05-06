# Composition

## Theory

**Inheritance** answers **is-a** (**`Dog` is an `Animal`**). **Composition** answers **has-a** or **uses-a**: one object **contains** or **uses** another type.

```python
class Engine:
    def start(self):
        return "vroom"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

**`Car`** does **not** inherit from **`Engine`**—it **owns** an **`Engine`**. This avoids deep class hierarchies and keeps responsibilities small.

## Beginner-friendly notes

- Prefer composition when “specialization” isn’t natural—e.g. a **`Library`** **has** many **`Book`**s (usually a **`list`**) rather than **`Library`** inheriting from **`Book`**.
- You will still use **inheritance** sometimes; the skill is **choosing** the simpler story.

## Example

```python
class Grade:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

class ReportCard:
    def __init__(self):
        self.grades = []

    def add(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(g.score for g in self.grades) / len(self.grades)

rc = ReportCard()
rc.add(Grade("Math", 90))
rc.add(Grade("Art", 85))
print(rc.average())
```

## Expected output

```text
87.5
```

## Mini practice

1. Model **`Team`** with a **`list`** of **`Player`** objects (simple **`name`** field). Add **`add_player`** and **`roster`** method that **`print`**s names with a **`for`** loop.
2. Explain **has-a** vs **is-a** using **`Team`** / **`Player`** in one sentence.
3. (Stretch) Should **`Library`** inherit **`Book`**? Why or why not?

---

**End of Section 6 (Object-oriented programming).** Complete `homework.md`.
