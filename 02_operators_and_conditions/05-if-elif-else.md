# `if`, `elif`, `else`

## Theory

Programs often need to **choose** what to do based on a condition. In Python:

- **`if`** runs a block of code **only when** a condition is true.
- **`elif`** (short for “else if”) checks **another** condition if the previous ones failed. You can have zero or many `elif` parts.
- **`else`** runs a block when **none** of the `if` / `elif` conditions were true.

**Indentation** defines the blocks: everything indented under `if` belongs to that branch. Python uses indentation (usually 4 spaces), not braces like some languages.

A condition is an expression that evaluates to a **boolean** (`True` or `False`).

## Beginner-friendly notes

- **`=`** assigns; **`==`** compares for equality. Mixing them up is a common bug.
- Order matters: Python checks `if`, then first `elif`, then next `elif`, and so on. The **first** true branch wins; the rest are skipped.
- If you need **all** checks to run, use separate `if` statements, not `elif`.

## Example

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Below C"

print("Grade:", grade)
```

## Expected output

```text
Grade: B
```

## Mini practice

1. Set `temperature = 30`. If it is **25 or above**, print `"warm"`. Elif it is **15 or above**, print `"ok"`. Else print `"cold"`.
2. In the lesson’s grade example, change `score` to `76`, run the code, and check that the printed grade matches what you expect.

Continue with `06-nested-conditions.md`.
