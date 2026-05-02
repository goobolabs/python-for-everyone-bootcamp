# Section 5: File handling and error handling

This section covers **reading**, **writing**, and **appending** text files (with `encoding="utf-8"`), and handling failures with **`try` / `except` / `finally`** using **built-in** exception types (for example `FileNotFoundError`, `ValueError`).

## Learning goals

By the end of this section, you will be able to:

- Open text files safely with a **`with`** block and a clear **mode** (`"r"`, `"w"`, `"a"`).
- Read contents whole, or **line by line**, and reason about **working directory** and paths.
- Write and append without accidentally wiping data when you meant to keep it.
- Catch **specific** exceptions and use **`finally`** when cleanup should always run.
- **`raise ValueError`** with a clear message when input breaks a simple rule you define.

## Topic summary (order of lessons)

| Order | Topic | File |
|------:|-------|------|
| 1 | Reading files | `01-reading-files.md` |
| 2 | Writing files | `02-writing-files.md` |
| 3 | Appending files | `03-appending-files.md` |
| 4 | `try`, `except`, `finally` | `04-try-except-finally.md` |

Work through the lessons in order. Each lesson ends with a small practice task. After the section, complete the assignments in `homework.md`.

## How to use this section

1. Read one lesson file from top to bottom.
2. Type the example code yourself (do not only copy-paste).
3. Compare your output to the **Expected output** in the lesson.
4. Do the **Mini practice** before moving on.

When you are ready, open `01-reading-files.md` and begin.

## Prerequisites

Sections 1–4: variables, control flow, collections, and functions (`04_functions`). You should be comfortable with **strings** and **`for`** loops from earlier sections.
