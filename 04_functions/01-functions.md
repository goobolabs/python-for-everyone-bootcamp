# Functions

## Theory

A **function** is a named block of code you can **call** many times. In Python you define one with **`def`**:

```python
def name(parameters):
    # body (indented)
    ...
```

**Benefits:** reuse, readability, testing one piece at a time, and clearer structure for larger programs.

**Calling:** `name(arguments)` runs the body with parameters bound to the passed values.

## Beginner-friendly notes

- Function names use **`snake_case`** in Python (PEP 8).
- The body must be **indented** (usually 4 spaces).
- Define functions **before** you call them in the same file (or import them from another module).

## Example

```python
def greet(name):
    print("Hello,", name)

def add(a, b):
    return a + b

greet("Sam")
print(add(2, 3))
```

## Expected output

```text
Hello, Sam
5
```

## Mini practice

1. Write `def square(n):` that returns `n * n`. Print `square(7)`.
2. Write `def shout(text):` that prints `text` in uppercase (hint: `.upper()`). Call it with your name.
3. Explain in one sentence: what is the difference between **defining** and **calling** a function?

Continue with `02-parameters.md`.
