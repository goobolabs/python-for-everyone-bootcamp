# Variables

## Theory

A **variable** is a **name** that refers to a value stored in memory. In Python, you create a variable by **assignment**: `name = value`.

Rules and conventions:

- Names can include letters, digits, and underscores; they **cannot** start with a digit.
- Names are **case-sensitive**: `score` and `Score` are different.
- **Style:** use `snake_case` for variable names (words separated by underscores)—this is the common Python style ([PEP 8](https://peps.python.org/pep-0008/)).

You can **reassign** a variable: the name then refers to a new value.

## Beginner-friendly notes

- Think of a variable as a **label** on a box, not the box itself. `x = 5` means “let the name `x` refer to the integer 5.”
- Choose names that describe purpose: `total_price` is clearer than `tp`.
- Avoid using names that shadow built-ins if you can (`list`, `str`, `sum`, etc.)—we will learn what those are.

## Example

```python
student_name = "Amina"
points = 100
points = points + 10

print(student_name)
print(points)
```

## Expected output

```text
Amina
110
```

## Mini practice

1. Create variables `city` and `country` with string values you like. Print them on one line separated by a comma.
2. Create `counter = 0`. Add 1 to `counter` three times using `counter = counter + 1`. Print `counter` at the end (should be `3`).

Continue with `08-data-types.md`.
