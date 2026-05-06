# Homework — Section 2: Operators and conditions

Complete these tasks after you finish all lessons in this section (through `06-nested-conditions.md`). They follow the same ideas as the **Mini practice** steps in each lesson—just a bit longer and using `input()` where it helps.

Submit according to your instructor’s format (files, screenshots, or a short write-up).

---

## Assignment 1: Temperature from the user

Write `temperature_input.py` that:

1. Asks the user for a **temperature** as an integer (use `input()` and `int(...)`).
2. Uses **`if` / `elif` / `else`** with the **same thresholds** as the `if-elif-else` lesson mini practice: **25 or above** → print `"warm"`; **15 or above** (but below 25) → print `"ok"`; otherwise → print `"cold"`.

**Deliverable:** `temperature_input.py` + one example run pasted (any integer you type is fine).

---

## Assignment 2: Nested questions (admin gate)

Write `admin_gate.py` that:

1. Asks for a **username** with `input()`.
2. If the username is **`"admin"`**, asks for a **password**. If the password is **`"secret"`**, prints **`"Access granted"`**. Otherwise prints **`"Wrong password"`**.
3. If the username is **not** `admin`, prints **`"Unknown user"`** and does **not** ask for a password.

This matches the nested-conditions lesson mini practice, using the same strings.

**Deliverable:** `admin_gate.py` + two example runs: one that reaches `"Access granted"`, and one that shows `"Unknown user"` or `"Wrong password"`.

---

## Assignment 3: Logical combinations (`and` / `or`)

Write `logic_permissions.py` that:

1. Asks the user for their **age** as an integer (`input()` and `int(...)`).
2. Asks whether a **parent or guardian is with them**, using a single letter answer: the user types **`y`** or **`n`** (compare the string to `"y"`).
3. Prints **`"OK to enter"`** if this rule is satisfied: **age is 13 or older**, **or** (**age is at least 10** **and** the parent answer is **`y`**). Otherwise prints **`"Sorry, not this time"`**.

Use **`and`** and **`or`** in your condition (add **parentheses** so the rule is easy to read).

**Deliverable:** `logic_permissions.py` + two example runs: one run that prints `"OK to enter"` and one that prints `"Sorry, not this time"`.

---

## Self-check

- [ ] Every `if` / `elif` / `else` lines up the way you intend (watch indentation).
- [ ] You used `==` for comparisons, not `=` inside conditions.
- [ ] When you mix `and` and `or`, parentheses make the rule match what you intend.

After you finish this homework, you are ready to go to the **next** section of the bootcamp.
