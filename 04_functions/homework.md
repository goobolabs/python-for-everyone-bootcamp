# Homework — Section 4: Functions and Modules

Complete these tasks after you finish **all** lessons in this section (`01-functions.md` through `06-scope.md`). The assignments follow the lesson order.

Submit according to your instructor's format (files, screenshots, or a short write-up).

| Assignment | Main lesson file |
|------------|------------------|
| 1 - Build and call functions | `01-functions.md` |
| 2 - Parameters vs arguments | `02-parameters.md` |
| 3 - Return values | `03-return-values.md` |
| 4 - Default arguments | `04-default-arguments.md` |
| 5 - `*args` and `**kwargs` | `05-args-and-kwargs.md` |
| 6 - Scope practice | `06-scope.md` |

---

## Assignment 1: Build and call functions

**Lesson:** `01-functions.md`

Create `greetings.py` that:

1. Defines `greet(name)` that prints `Hello, <name>!`.
2. Calls `greet(...)` at least **three** times with different names.
3. Defines a second function `bye(name)` and calls it at least once.

**Deliverable:** `greetings.py` + output.

---

## Assignment 2: Parameters vs arguments

**Lesson:** `02-parameters.md`

Create `calculator_calls.py` that:

1. Defines `multiply(a, b)` and returns `a * b`.
2. Calls it using **positional arguments** once (example: `multiply(3, 4)`).
3. Calls it using **keyword arguments** once (example: `multiply(b=5, a=2)`).
4. Prints the result of each call with a short label.

Add one short comment in the file explaining the difference between **parameters** and **arguments** in your own words.

**Deliverable:** `calculator_calls.py` + output.

---

## Assignment 3: Return values

**Lesson:** `03-return-values.md`

Create `grade_tools.py` that:

1. Defines `is_passing(score)` that returns `True` when score is `>= 50`, else `False`.
2. Defines `grade_label(score)` that returns `"A"`, `"B"`, `"C"`, or `"F"` using a simple rule you choose (document your rule in a comment).
3. Tests both functions with at least **four** different scores and prints clear results.

**Deliverable:** `grade_tools.py` + output.

---

## Assignment 4: Default arguments

**Lesson:** `04-default-arguments.md`

Create `messages.py` that:

1. Defines `send_message(name, message="Welcome!")`.
2. Prints one formatted line showing who receives the message.
3. Calls the function once with only `name` (use default message).
4. Calls the function again with both `name` and a custom message.
5. Adds one comment warning why mutable defaults (like `[]` or `{}`) can be risky.

**Deliverable:** `messages.py` + output.

---

## Assignment 5: Flexible arguments (`*args`, `**kwargs`)

**Lesson:** `05-args-and-kwargs.md`

Create `flexible_report.py` that includes:

1. `def total(*numbers):` that returns the sum of all numbers passed.
2. `def profile(**info):` that prints each key-value pair on its own line.
3. At least **three** calls to `total(...)` (including one call with no numbers).
4. At least **two** calls to `profile(...)` with different keyword fields.

**Deliverable:** `flexible_report.py` + output.

---

## Assignment 6: Scope practice

**Lesson:** `06-scope.md`

Create `scope_demo.py` that:

1. Defines a global variable `course_name = "Python Bootcamp"`.
2. Defines a function that creates a local variable with a similar name and prints it.
3. Prints the global value before and after calling the function.
4. Adds a brief comment explaining local vs global scope in this example.

**Important:** Do not mutate globals with `global` in this assignment; keep it focused on reading/printing scope behavior.

**Deliverable:** `scope_demo.py` + output.

---

## Self-check

- [ ] I can explain **parameters** vs **arguments** with my own example.
- [ ] I know when to use `return` versus printing directly.
- [ ] I can use default arguments safely and avoid mutable defaults.
- [ ] I can read and write function calls with `*args` and `**kwargs`.
- [ ] I can identify whether a name is local or global in simple scripts.

After this homework, review all six lesson files once more before **Section 5** — `05_file_handling_and_error_handling`.
