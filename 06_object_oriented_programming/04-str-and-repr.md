# `__str__` and `__repr__`

## Theory

Printing an object with **`print(obj)`** calls **`obj.__str__()`** for a **human-friendly** string. In classes you define:

```python
def __str__(self):
    return f"Book({self.title})"
```

**`__repr__`** should ideally return a string that **looks like code** you could eval (ideal); at minimum it should be **unambiguous** for debugging. If **`__str__`** is missing, Python may fall back to **`__repr__`**.

For beginners: implement **`__str__`** first so **`print`** looks nice; add **`__repr__`** when you want **`repr(obj)`** to show useful detail.

## Beginner-friendly notes

- These names start and end with **double underscores** (“dunder” methods).
- Keep **`__str__`** short—what you’d show a user in a log line.

## Example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

p = Point(2, 3)
print(p)
print(repr(p))
```

## Expected output

```text
Point(2, 3)
Point(2, 3)
```

## Mini practice

1. Add **`__str__`** to **`Book`** from earlier lessons so **`print(book)`** shows **`Title by Author`** (pick your format).
2. Try **`print(repr(book))`** before and after adding **`__repr__`**—what changes?
3. Implement **`__repr__`** for **`Point`** that differs slightly from **`__str__`** (for example include **`Point`** prefix only in **`repr`**).

Continue with `05-inheritance.md`.
