# Data types

## Theory

Every value in Python has a **type**. Types describe what kind of data you have and what operations are allowed.

Core types for beginners:

| Type | Meaning | Example literals |
|------|---------|------------------|
| `int` | Whole numbers | `0`, `-3`, `42` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `str` | Text (strings) | `"hello"`, `'Python'` |
| `bool` | Truth values | `True`, `False` |

You can inspect a value’s type with **`type()`**:

```python
type(42)       # <class 'int'>
type(3.14)     # <class 'float'>
type("hi")     # <class 'str'>
type(True)     # <class 'bool'>
```

**Strings** can use single or double quotes as long as they match: `'hi'` and `"hi"` are the same string.

The built-in function **`len(s)`** returns how many characters are in a string: `len("hello")` is `5`.

## Beginner-friendly notes

- `2` (int) and `2.0` (float) are different types even though they feel “equal” in math.
- For now, remember: **numbers** for math, **strings** for text, **booleans** for conditions (next section).
- Errors like `TypeError` often mean you mixed types in a way Python does not allow (e.g. adding a string to an integer without converting).

## Example

```python
age = 20
price = 19.99
label = "Ticket"
active = True

print(type(age), age)
print(type(price), price)
print(type(label), label)
print(type(active), active)
```

## Expected output

```text
<class 'int'> 20
<class 'float'> 19.99
<class 'str'> Ticket
<class 'bool'> True
```

## Mini practice

1. Create one variable of each type (`int`, `float`, `str`, `bool`). Print each value and its `type(...)` on the same line.
2. Predict then run: what is `type("42")`? What is `type(42)`? Write one sentence explaining the difference.

Continue with `09-input-output.md`.
