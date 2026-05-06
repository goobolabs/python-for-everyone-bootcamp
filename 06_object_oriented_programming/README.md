# Section 6: Object-oriented programming

This section introduces **classes** and **objects**: grouping data with behavior, **instance methods**, **class vs instance** data, readable **`__str__`/`__repr__`**, **inheritance**, **`@dataclass`**, and **composition**. Everything stays practical and small—no metaclasses or deep theory.

## Learning goals

By the end of this section, you will be able to:

- Define a **class**, build instances with **`__init__`**, and use **`self`** for instance data.
- Add **instance methods** that read or change an object’s state.
- Tell **class attributes** apart from **instance attributes** and spot basic pitfalls.
- Implement **`__str__`** (and understand **`__repr__`** at a glance).
- Subclass a parent class, **override** methods, and call **`super()`** for simple `__init__` chaining.
- Use **`@dataclass`** for data-focused types with less boilerplate.
- Prefer **composition** (“has-a”) for building bigger objects from smaller ones.

## Topic summary (order of lessons)

| Order | Topic | File |
|------:|-------|------|
| 1 | Classes and objects | `01-classes-and-objects.md` |
| 2 | Instance methods | `02-instance-methods.md` |
| 3 | Class and instance attributes | `03-class-and-instance-attributes.md` |
| 4 | `__str__` and `__repr__` | `04-str-and-repr.md` |
| 5 | Inheritance | `05-inheritance.md` |
| 6 | Dataclasses | `06-dataclasses.md` |
| 7 | Composition | `07-composition.md` |

Work through the lessons in order. Each lesson ends with a small practice task. After the section, complete the assignments in `homework.md`.

## How to use this section

1. Read one lesson file from top to bottom.
2. Type the example code yourself (do not only copy-paste).
3. Compare your output to the **Expected output** in the lesson.
4. Do the **Mini practice** before moving on.

When you are ready, open `01-classes-and-objects.md` and begin.

## Prerequisites

Sections 1–5: variables, control flow, collections, functions, and basic file/error handling. **`self`** in methods works like “the current object,” similar to passing that object into a function explicitly—your first lesson connects that idea.
