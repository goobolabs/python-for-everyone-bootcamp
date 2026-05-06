# Homework — Section 6: Object-oriented programming

Complete after **`01-classes-and-objects.md` through `07-composition.md`**. Tasks follow the lesson order in groups—each one is short.

Submit according to your instructor's format (files, screenshots, or a short write-up).

| Assignment | Lessons | File to submit |
|------------|---------|----------------|
| 1 — First class | `01-classes-and-objects.md` | `hw_pet.py` |
| 2 — Methods | `02-instance-methods.md` | `hw_counter.py` |
| 3 — Shared vs own data | `03-class-and-instance-attributes.md` | `hw_team.py` |
| 4 — Printing objects | `04-str-and-repr.md` | `hw_point.py` |
| 5 — Parent and child class | `05-inheritance.md` | `hw_animal.py` |
| 6 — Dataclass + composition | `06-dataclasses.md`, `07-composition.md` | `hw_shelf.py` |

For a **course-wide** capstone that uses Sections **1–6** together, see **Assignment 3** in [`assignments/03-personal-catalog.md`](../assignments/03-personal-catalog.md).

---

## Assignment 1: First class

**Lesson:** `01-classes-and-objects.md`

In **`hw_pet.py`**, define **`class Pet`** with **`__init__(self, name, species)`** (both strings). Create **two** pets and **`print`** each **`name`** on its own line.

**Deliverable:** `hw_pet.py` + output.

---

## Assignment 2: Methods

**Lesson:** `02-instance-methods.md`

In **`hw_counter.py`**, define **`class Counter`** with **`count`** starting at **`0`** and a method **`bump(self)`** that adds **`1`** to **`count`**. Create one counter, call **`bump`** three times, **`print`** **`count`**.

**Deliverable:** `hw_counter.py` + output.

---

## Assignment 3: Shared vs own data

**Lesson:** `03-class-and-instance-attributes.md`

In **`hw_team.py`**, define **`class Player`** with **class attribute** **`game = "training"`** (same for everyone). In **`__init__`**, set **`self.username`** (string). Make **two** players with different **`username`** values. **`print`** **`game`** twice (same value) and **`print`** both **`username`**s.

**Deliverable:** `hw_team.py` + output.

---

## Assignment 4: Printing objects

**Lesson:** `04-str-and-repr.md`

In **`hw_point.py`**, define **`class Point`** with **`x`** and **`y`**. Add **`__str__(self)`** so **`print(Point(2, 5))`** shows something clear (your format—note it in a comment).

**Deliverable:** `hw_point.py` + output.

---

## Assignment 5: Parent and child class

**Lesson:** `05-inheritance.md`

In **`hw_animal.py`**, define **`class Animal`** with **`__init__(self, name)`** storing **`self.name`**. Define **`class Dog(Animal)`** with **`__init__(self, name, breed)`**: call **`super().__init__(name)`** and set **`self.breed`**. Create one **`Dog`** and **`print`** **`name`** and **`breed`**.

**Deliverable:** `hw_animal.py` + output.

---

## Assignment 6: Dataclass + composition

**Lessons:** `06-dataclasses.md`, `07-composition.md`

In **`hw_shelf.py`**:

1. Use **`@dataclass`** for **`Book`** with **`title: str`** and **`author: str`**.
2. Define **`class Shelf`** with **`self.books = []`**, **`add(self, book)`**, and **`titles(self)`** that **`return`** a **list** of strings (each book’s **`title`**)—build it with a **`for`** loop.

Create **two** **`Book`** instances, **`Shelf()`**, **`add`** both, **`print`** **`titles()`**.

**Deliverable:** `hw_shelf.py` + output.

---

## Self-check

- [ ] I used **`__init__`** and **`self`** for instance fields.
- [ ] I wrote at least one **method** and one **`super().__init__(...)`** chain.
- [ ] I used **`@dataclass`** and a class that **holds** a list of another type.
