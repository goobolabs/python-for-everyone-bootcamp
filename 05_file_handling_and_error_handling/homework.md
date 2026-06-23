# Homework — Section 5: File handling and error handling

Complete these tasks after you finish **all** lessons, from `01-reading-files.md` through `04-try-except-finally.md`. Each assignment matches the lesson order below.

Submit according to your instructor's format (files, screenshots, or a short write-up).

| Assignment | Main lesson file |
|------------|------------------|
| 1 — Read and summarize | `01-reading-files.md` |
| 2 — Write a text file | `02-writing-files.md` |
| 3 — Journal (write + append) | `03-appending-files.md` |
| 4 — Errors, `finally`, and validation | `04-try-except-finally.md` |

---

## Assignment 1: Read and summarize a file

**Lesson:** `01-reading-files.md`

Create a text file `sample.txt` with several lines (commit or attach with homework). Write `summarize_file.py` that:

1. Opens `sample.txt` for **reading** with `encoding="utf-8"`.
2. Prints the **number of lines** and **number of characters** (including newlines, unless you document otherwise).

You will add **missing-file** handling in Assignment 4; for this task, assume the file exists.

**Deliverable:** `sample.txt`, `summarize_file.py`, output, and one sentence on why you used `utf-8`.

---

## Assignment 2: Write a text file

**Lesson:** `02-writing-files.md`

Create `write_note.py` that:

1. Opens a new file `note.txt` in **`"w"`** mode with `encoding="utf-8"`.
2. Writes at least **two** lines (for example a title line and one body line), each ending with `\n`.
3. Opens `note.txt` again for **reading** and prints its contents so you can verify what was written.

**Deliverable:** `write_note.py` + output (and optionally the resulting `note.txt`).

---

## Assignment 3: Write vs append (journal)

**Lesson:** `03-appending-files.md`

Create `journal.py` that:

1. **Writes** a new file `notes.txt` with a header line using **`"w"`** (overwrite is OK the first time).
2. **Appends** two more lines—either in a second run of the script **or** two append operations in one script. Add a short **comment** explaining which approach you used.
3. Prints the final file contents from Python (read back after writing).

**Deliverable:** `journal.py` + final `notes.txt` content (or pasted output).

---

## Assignment 4: Errors, `finally`, and validation

**Lesson:** `04-try-except-finally.md`

### Part A — Safe read

Create `safe_read.py` that:

1. Tries to open a file path (use `sample.txt` or a variable) for reading with `encoding="utf-8"`.
2. Uses **`try` / `except FileNotFoundError`** to print a clear message if the file is missing (no bare `except:`).
3. Uses **`finally`** to print one line such as `"done with open attempt"` so it runs whether the file existed or not.

Show **two** runs: file present, and missing/bad path so the friendly message appears.

### Part B — Positive integer with `ValueError`

Create `parse_positive.py` with:

1. A function `parse_positive_int(text)` that strips whitespace, converts with `int(...)`, and **raises `ValueError`** with a clear message if the value is `<= 0` (or if conversion fails—let `int` raise for non-numeric text).
2. A small `main` (or main block) that reads user input in a loop and catches **`ValueError`** until a valid **positive** integer is entered.

Use only **built-in** exceptions (`ValueError`); do not define your own exception classes.

**Deliverable:** `safe_read.py`, `parse_positive.py`, sample output / transcripts for both.

---

## Self-check

- [ ] You know when to open with `"r"` vs `"w"` vs `"a"`.
- [ ] You avoid bare `except:` in real code.
- [ ] You can read a traceback enough to find **line number** and **exception type**.
- [ ] You can **`raise`** and **`except`** `ValueError` for a simple validation rule.

Next: **Section 6** — `06_object_oriented_programming` (Object-oriented programming).
