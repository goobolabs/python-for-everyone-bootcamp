# Pseudocode and Flow Thinking

## Theory

**Pseudocode** is informal, human-readable steps that describe an algorithm **without** full programming syntax. It helps you **plan** before you write real code.

**Flow** means the **order** of operations and decisions: what happens first, what happens next, and what branches or repeats. Later you will write real `if` and loops; for now you practice thinking clearly.

Example pseudocode for “greet the user”:

```text
ask user for their name
store the answer in a variable called name
print a greeting that uses name
```

Same idea for a tiny calculation:

```text
read two numbers A and B
set sum = A + B
print sum
```

This is **algorithmic thinking**: break the problem into small, ordered steps. Then each step maps to one or a few lines of Python.

## Beginner-friendly notes

- Use **indentation** in pseudocode to show “inside” a step (like nested actions)—it previews how Python uses indentation.
- If you cannot say the steps in English (or your teaching language), you are not ready to code them—**clarify first**.
- Names like `name`, `total`, `score` are good placeholders before you open an editor.

## Example

**Pseudocode:**

```text
set count to 0
add 1 to count
add 1 to count
print count
```

**Same idea in Python:**

```python
count = 0
count = count + 1
count = count + 1
print(count)
```

## Expected output

```text
2
```

## Mini practice

1. Write **pseudocode only** (no Python) for: read a number, multiply it by 2, print the result.
2. Translate your pseudocode into Python and run it with **one** number you type (you may use `input` and `int` if you already peeked ahead, or hard-code a variable for this drill).
3. Write pseudocode for: “if the score is at least 50, print pass; else print keep practicing.” (You will implement real `if` in Section 2: Operators and conditions.)

When you are done, continue with `04-what-is-python.md`.
