# Assignment 2: Simple study log

**Due:** Saturday, May 2, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** One short program, **`study_log.py`**, that uses a little of **each** section (1–5)—nothing advanced.

**Sections covered:** **1 — Foundations**, **2 — Operators and conditions**, **3 — Collections & loops**, **4 — Functions**, **5 — Files & error handling**

You save **one-line notes** in a list. The user can add a note, print all notes, then quit. When the program **starts**, it tries to read old notes from a text file. When the user **quits**, it writes the list back to the same file. If the file is not there the first time, the program just starts with an empty list.

---

## Ideas from each section (keep it basic)

| Section | Use something simple like… |
|--------|---------------------------|
| **1** | Comments at the top, variables, `print`, `input` |
| **2** | `if` / `elif` / `else` for a small text menu (`"1"`, `"2"`, `"3"`) |
| **3** | A **list** of strings; a **`for`** loop to print every note |
| **4** | Two **`def`** helpers (below) **plus** `main()`; `if __name__ == "__main__": main()` |
| **5** | `with open(..., encoding="utf-8")`; `try` / `except FileNotFoundError` when loading |

**Two helper functions (example names—you can match these or use the same idea):**

- `load_notes(path)` — open `path` for **reading**, return a **list** of lines (strip newlines). If **`FileNotFoundError`**, return `[]`.
- `save_notes(path, notes)` — open `path` for **writing**, write each string in `notes` on its **own line** (`\n`).

Put the **menu loop** inside **`main()`** (add / list / quit).

---

## Requirements

Submit **`study_log.py`** only.

1. Top of file: **comment** with your name (or alias) and what the program does.
2. **Menu:** `print` three options, e.g. **1 = add**, **2 = list**, **3 = quit**. Use `if` / `elif` / `else` on the **`input()`** string (compare to `"1"`, `"2"`, `"3"`—no need for `int()`).
3. **List:** Store notes as a **`list`** of **`str`**. **Add** = `append` what the user types. **List** = **`for`** loop over the list and `print` each note.
4. **Start:** Before the menu, `notes = load_notes("notes.txt")` (or your file name). **`load_notes`** must use **`try` / `except FileNotFoundError`** and return **`[]`** if the file is missing.
5. **Quit:** When the user picks quit, call **`save_notes`**, then **exit** the loop (use **`break`** or **`return`** from `main`). Do **not** use a bare `except:` anywhere.
6. **`main()`** runs a **`while True:`** menu until **quit**; at the bottom of the file:

   ```python
   if __name__ == "__main__":
       main()
   ```

**Optional:** Ask for the user’s **name** once at the start and use it in one `print` (like Assignment 1).

---

## Example (shape only)

```text
1) Add note  2) List  3) Quit
Pick: 1
Note: Learned about lists

1) Add note  2) List  3) Quit
Pick: 2
Learned about lists

1) Add note  2) List  3) Quit
Pick: 3
Bye!
```

---

## Submitting

Follow **`submissions/README.md`**: add **`study_log.py`** under **`submissions/<your-github-username>/`**, open a pull request.

---

## Checklist

- [ ] Runs with `python study_log.py` (or `python3`).
- [ ] Menu uses **`if` / `elif` / `else`**; notes are a **`list`**; **`for`** to list them.
- [ ] **`load_notes`** + **`save_notes`** + **`main()`**; **`if __name__ == "__main__":`**.
- [ ] Load uses **`try` / `except FileNotFoundError`**; save/read uses **`encoding="utf-8"`**.
