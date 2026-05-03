# Homework — Section 3: Collections, loops, and methods

Complete these tasks after you finish **all** lessons, from `01-lists.md` through `08-common-methods.md`. They follow the same section order as the table below.

Submit according to your instructor’s format (files, screenshots, or a short write-up).

| Assignment | Main lesson file |
|------------|------------------|
| 1 — List toolkit | `01-lists.md` |
| 2 — Coordinates | `02-tuples.md` |
| 3 — Unique words | `03-sets.md` |
| 4 — Phonebook | `04-dictionaries.md` |
| 5 — Iterate and slice | `05-for-loops.md` (uses list slicing from **Lists** too) |
| 6 — `while` and input | `06-while-loops.md` |
| 7 — `break` / `continue` | `07-break-continue-pass.md` |
| 8 — String methods | `08-common-methods.md` |

---

## Assignment 1: List toolkit

**Lesson:** `01-lists.md`

Create `list_toolkit.py` that:

1. Builds a list of at least **five** strings (e.g. course names or cities).
2. Prints the **first** and **last** item using indexing (hint: negative index for last).
3. **Appends** one new string and prints the list.
4. **Removes** one item by value (`.remove(...)`) or by index (`.pop(...)`); say which you used in a **comment**.
5. Prints the **length** with `len(...)`.

**Deliverable:** `list_toolkit.py` + output.

---

## Assignment 2: Coordinates (tuple + unpacking)

**Lesson:** `02-tuples.md`

Create `coordinates.py` that:

1. Defines a tuple `point` representing `(x, y)` with two numbers.
2. **Unpacks** it into variables `x` and `y` and prints them.
3. Defines a tuple with **one** element (remember the comma) and prints its type and value.

**Deliverable:** `coordinates.py` + output.

---

## Assignment 3: Unique words (set)

**Lesson:** `03-sets.md`

Create `unique_words.py` that:

1. Starts with a list containing **duplicate** strings, e.g. `["go", "python", "go", "code", "python"]`.
2. Builds a **set** from the list to get unique words.
3. Prints the unique words (order may vary—that is OK).
4. Checks membership: print whether `"python"` is in the set using `in`.

**Deliverable:** `unique_words.py` + output.

---

## Assignment 4: Phonebook (dictionary)

**Lesson:** `04-dictionaries.md`

Create `phonebook.py` that:

1. Uses a **dictionary** mapping names (strings) to phone numbers (strings).
2. Adds at least **three** entries.
3. Uses **`.get(...)`** to look up a name that **exists** and a name that **does not** exist (use a default like `"unknown"`).
4. Loops with **`for name in ...`** and prints one line per person (you may use just keys, or show **`.items()`** in a second small loop—your choice, but use the dict in two different ways: lookup + loop).

**Deliverable:** `phonebook.py` + output.

---

## Assignment 5: Iterate and slice (`for` + `range` + `enumerate`)

**Lesson:** `05-for-loops.md`

Create `iterate_practice.py` that:

1. Builds `nums = list(range(10))` (0 through 9). Prints **every second** value starting at index 0 using **slicing** with a **step** (e.g. `nums[::2]`).
2. Prints `nums` **reversed** using a slice with a **negative step** (e.g. `[::-1]`) **or** `reversed(...)`—say which in a **comment**.
3. Uses a **`for`** loop with **`range(3, 8)`** and prints each number on its own line.
4. Uses **`enumerate`** on a list of at least **three** words and prints `index: word` on each line.
5. Builds a small **dict** (e.g. two key–value pairs) and uses **`for k, v in d.items():`** to print each pair on one line.

**Deliverable:** `iterate_practice.py` + output.

---

## Assignment 6: `while` and user input

**Lesson:** `06-while-loops.md`

Create `while_input.py` that:

1. Uses a **`while`** loop. Ask the user to type a line of text. Keep asking until they type exactly **`done`** (lowercase is fine, or document if you accept `Done`).
2. For each line that is **not** `done`, print it back (e.g. `You typed: ...`).
3. After they type `done`, print a short goodbye message.

**Deliverable:** `while_input.py` + example run (a few lines of input, then `done`).

---

## Assignment 7: `break` and `continue`

**Lesson:** `07-break-continue-pass.md`

Create `loop_control.py` that:

1. Uses **`for n in range(15):`**. Print `n`, but use **`break`** to stop the loop the first time `n` is **greater than 6** (so you should see 0 through 7 or stop right after 6—your code should be easy to read; pick one rule and state it in a **comment**).
2. Uses **`for n in range(10):`**. Use **`continue`** to **skip** printing when `n` is **4** (print all other values 0–9 except you skip 4’s print).
3. Includes an **`if False:`** block whose body is only **`pass`** (so the file is still valid).

**Deliverable:** `loop_control.py` + output.

---

## Assignment 8: String and list methods

**Lesson:** `08-common-methods.md`

Create `text_cleanup.py` that:

1. Sets `line = "  Hello, you, WORL D "` (or your own string with extra spaces and commas).
2. Uses **`.strip()`** to trim ends, then **`.lower()`** (or just strip)—print the result.
3. Uses **`.split(",")`** to split into parts; print the resulting **list**.
4. Uses **`.append(...)`** on a list you build: start with an empty list, append three strings, then print the list.

**Deliverable:** `text_cleanup.py` + output.

---

## Self-check

- [ ] **List** vs **tuple** vs **set** vs **dict**: you can say one sentence for when you’d use each.
- [ ] You can use **slicing** and **`range`** / **`enumerate`** / **`.items()`** without mixing up “stop is exclusive” rules.
- [ ] You know when **`for`** is clearer than **`while`**, and you can use **`break`** / **`continue`** on purpose, not by accident.
- [ ] You can find **methods** on `str` and `list` when you need them (docs or `help`).

Next: **Section 4** — `04_functions` (Functions and modules), then **Section 5** — `05_file_handling_and_error_handling`.
