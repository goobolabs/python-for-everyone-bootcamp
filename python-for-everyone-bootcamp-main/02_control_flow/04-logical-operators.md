# Logical operators

## Theory

**Logical operators** combine boolean values:

| Operator | Meaning |
|----------|---------|
| `and` | True if **both** sides are true |
| `or` | True if **at least one** side is true |
| `not` | True if the operand is false |

Python uses **short-circuit** evaluation:

- For `a and b`, if `a` is false, `b` is not evaluated.
- For `a or b`, if `a` is true, `b` is not evaluated.

**Truthiness:** Later you will see values like `""` or `0` used where a boolean is expected. For now, use **explicit comparisons** (`==`, `!=`, `<`, …) so every `and` / `or` / `not` works on clear `True` / `False` results. The next lesson shows how to **branch** with `if` using exactly these expressions.

## Beginner-friendly notes

- Use **parentheses** when mixing `and` / `or` so the meaning is obvious: `(a or b) and c` vs `a or (b and c)`.
- `not (x == y)` is the same as `x != y` for numbers and strings; use whichever reads better.

## Example

Each expression below is either `True` or `False`. `print` shows that value—no `if` yet.

```python
age = 25
has_id = True
print(age >= 18 and has_id)

age = 16
has_id = True
print(age >= 18 and has_id)

score = 85
print(score < 60 or score > 100)

score = 120
print(score < 60 or score > 100)

ready = False
print(not ready)
```

## Expected output

```text
True
False
False
True
True
```

## Mini practice

1. Set `username = "alex"` and `logged_in = True`. Print a single expression (using `and` and `==`) that is **`True`** only when the username is **`"alex"`** and `logged_in` is **`True`**.
2. Set `day = "Saturday"`. Print whether it is a weekend day using **`or`** and two comparisons to **`"Saturday"`** and **`"Sunday"`**. Change `day` to **`"Monday"`** and run again so you see `False`.

Continue with `05-if-elif-else.md`, where you will use expressions like these inside `if` to run different code for each case.
