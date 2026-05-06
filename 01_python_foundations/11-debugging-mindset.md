# Debugging Mindset

## Theory

**Debugging** means finding and fixing **why** the program behaves wrong. Beginners often feel they “are bad at coding” after the first errors—they are not; **errors are normal** and even experienced developers debug every day.

A productive mindset:

1. **Expect mistakes.** Typos, wrong indentation, and wrong values are part of learning.
2. **Read the message.** Python often prints an **error type** and **line number**—start there.
3. **Reproduce.** Run the smallest example that shows the bug. Change one thing at a time.
4. **Explain the code** to someone (or a rubber duck): “This line should do X because…” Often you spot the gap.
5. **Compare** to working examples from lessons—line by line.

Common beginner issues (preview):

- **`SyntaxError`** — punctuation or structure wrong (`:` missing, parenthesis not closed).
- **`NameError`** — using a variable name that was never assigned.
- **`TypeError`** — operation on the wrong kind of data (e.g. adding number + text without converting).

You will deepen error handling in a later section; here the goal is **calm, systematic checking**.

## Beginner-friendly notes

- **Print debugging:** temporarily `print("here", variable)` to see values mid-run.
- **Save** before run; **read** output from the top of the traceback down to the error line.
- Google the error message in quotes—often someone had the same first-week issue.

## Example

This code has a deliberate bug (`message` misspelled on the last line):

```python
message = "Hi"
print(mesage)
```

## Expected output

Python raises an error (exact text may vary slightly):

```text
NameError: name 'mesage' is not defined
```

**Fix:** spell `message` the same way everywhere.

## Mini practice

1. Type the buggy example, run it, and confirm you see a `NameError`. Fix it and run again.
2. Introduce a **new** bug on purpose: remove one parenthesis from `print("test")`. Read the error type (`SyntaxError`). Fix it.
3. Write **three** checks you will run next time your program “does nothing” or crashes (e.g. “Did I save?” “Which file did I run?” “What line does the error point to?”).

---

**End of Section 1 lessons.** Complete `homework.md` before starting **Section 2: Operators and conditions** (`02_operators_and_conditions/`).
