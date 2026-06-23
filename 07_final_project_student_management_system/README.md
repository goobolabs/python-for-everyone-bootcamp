# Student management — final project

Small CLI demo that uses ideas from **Sections 1–6** of the bootcamp: comments, **`print`** / **`input`**, conditions, lists and loops, functions and **`main()`**, files (UTF-8), **`try` / `except`** on bad input, **`__str__`** on a class, **`@dataclass`**, and composition.

**Python 3.10+** (uses `|` in type hints, e.g. `str | None`).

## Run

```bash
cd 07_final_project_student_management_system
python main.py
```

## What's where

| Path | Purpose |
|------|---------|
| `main.py` | Menu |
| `models/students.py` | `Student` (one pupil) + `School` (all pupils in memory) |
| `utils/storage.py` | Read/write `data/students.txt` |
| `data/students.txt` | Saved roster |

## Menu

Add, list, remove, search, **update** (change name and/or grades), save, quit (quit saves).

When updating grades, type **`none`** to clear all grades for that pupil.

## Data file

UTF-8 text. Optional lines starting with `#`. Then a header row **`id|name|grades`**, then one pupil per row (pipes separate columns). **Grades** are comma-separated numbers, or empty.
