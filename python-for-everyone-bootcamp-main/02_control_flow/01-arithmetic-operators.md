# Arithmetic operators

## Theory

Python supports familiar math **operators** for numbers (`int` and `float`):

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `3 + 4` → `7` |
| `-` | Subtraction | `10 - 3` → `7` |
| `*` | Multiplication | `6 * 7` → `42` |
| `/` | Division (always float in Python 3) | `7 / 2` → `3.5` |
| `//` | Floor division (integer division toward negative infinity) | `7 // 2` → `3` |
| `%` | Modulo (remainder) | `7 % 2` → `1` |
| `**` | Power | `2 ** 3` → `8` |

**Order of operations** follows normal math rules; use **parentheses** `(...)` when you want to force clarity.

**String note:** `+` can **concatenate** strings (`"a" + "b"` → `"ab"`). `*` with an integer repeats a string (`"ha" * 3` → `"hahaha"`). Mixing strings and numbers without conversion causes `TypeError`.

## Beginner-friendly notes

- Use `/` when you want true division; use `//` when you want “how many whole times does it fit?” (for positive numbers, think “quotient”).
- `%` is useful for “every nth item” patterns (later loops).
- When in doubt, add parentheses—readable beats clever.

## Example

```python
a = 17
b = 5

print("a + b =", a + b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("2 ** 10 =", 2 ** 10)

text = "Go "
print(text * 3)
```

## Expected output

```text
a + b = 22
a / b = 3.4
a // b = 3
a % b = 2
2 ** 10 = 1024
Go Go Go 
```

## Mini practice

1. Set two number variables and print their **sum** (for example `3` and `4`, then print `7`).
2. Print the value of `10 // 3` on one line (see how `//` differs from `/` in the lesson table).
3. Print `"Hi! "` three times in one expression using `*` on a string.

Continue with `02-assignment-operators.md`.
