# Assignment 3: Personal catalog (Sections 1–6)

**Due:** Thursday, May 7, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** One program, **`catalog.py`**, that uses a **little from every section** (1–6)—same spirit as Assignment 1 (quiz) and Assignment 2 (study log), now including **classes** and **simple OOP**.

**Sections covered:** **1 — Foundations**, **2 — Operators and conditions**, **3 — Collections & loops**, **4 — Functions**, **5 — Files & error handling**, **6 — Object-oriented programming**

Build a tiny **catalog** (movies, games, or books—your pick). The user uses a **text menu** to **add** an item, **list** items, **save**, **quit**. Items are **objects** (see below), stored in a **list**. Data **loads** from a file at start and **saves** on quit.

---

## Ideas from each section (keep it basic)

| Section | Folder | Use something simple like… |
|--------|--------|----------------------------|
| **1** | `01_python_foundations` | Top-of-file **comment** (name + what it does), **`print`**, **`input`** |
| **2** | `02_operators_and_conditions` | **`if` / `elif` / `else`** on menu choice (`"1"` … `"4"`) |
| **3** | `03_collections_and_loops` | A **list** holding your items; **`for`** when listing |
| **4** | `04_functions` | **`load_catalog(path)`**, **`save_catalog(path, items)`**, **`main()`**; **`if __name__ == "__main__":`** |
| **5** | `05_file_handling_and_error_handling` | **`with open(..., encoding="utf-8")`**; **`try` / `except FileNotFoundError`** on load |
| **6** | `06_object_oriented_programming` | **`@dataclass`** **`CatalogItem`** (e.g. **`title`**, **`year`** as **`int`** OR **`kind`** as **`str`**—your fields); a **`Catalog`** **class** that **has** a **`list`** of **`CatalogItem`** and methods **`add_item`**, **`list_items`** (or similar) |

---

## Requirements

Submit **`catalog.py`** only.

1. **Comment** at the top: your name or alias, one line describing the program.
2. **`@dataclass CatalogItem`** — at least **two** fields (strings and/or one **`int`**—keep validation simple).
3. **`class Catalog`** — holds **`self.items`** (list); **`add`** puts a **`CatalogItem`** in the list; **`list_all`** **`print`**s each item in a readable way (use **`__str__`** on **`CatalogItem`** or format in the loop).
4. **`load_catalog(path, catalog)`** — read lines from a **text file** you design (e.g. **`title|year`** per line). **`split`** each line and build **`CatalogItem`** instances into **`catalog.items`**. Use **`try` / `except FileNotFoundError`**: if missing, **do nothing** (start empty). **`encoding="utf-8"`**.
5. **`save_catalog(path, catalog)`** — write **`catalog.items`** back using the **same** line format.
6. **`main()`** — **`while True:`** menu: **1 add** (ask for fields with **`input`**, create **`CatalogItem`**, **`catalog.add`**), **2 list**, **3 save**, **4 quit**. On **quit**, **`save`** then **`break`**. Before the loop: **`Catalog()`**, **`load_catalog(...)`**.
7. No bare **`except:`**.

**Optional:** **`__str__`** on **`CatalogItem`** for nicer **`print`**.

---

## Example (shape only)

```text
My catalog — movies
1) Add  2) List  3) Save  4) Quit
Pick: 1
Title: Python Story
Year: 2026

1) Add  2) List  3) Save  4) Quit
Pick: 2
Python Story (2026)

1) Add  2) List  3) Save  4) Quit
Pick: 4
Saved. Bye!
```

---

## Submitting

Follow **`submissions/README.md`**: add **`catalog.py`** under **`submissions/<your-github-username>/`**, open a pull request.

---

## Checklist

- [ ] Runs with **`python catalog.py`** (or **`python3`**).
- [ ] Menu + **list** + **`for`** listing; **functions** + **`main()`** + **`if __name__ == "__main__":`**.
- [ ] **Load/save** UTF-8 + **`FileNotFoundError`** on first run.
- [ ] **`@dataclass`** + **`Catalog`** **composition** (catalog **has** items).
