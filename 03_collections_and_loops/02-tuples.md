# Tuples

## Theory

A **tuple** is an **ordered** collection like a list, but **immutable**: after creation, you cannot add, remove, or replace items in place (no `.append`, no assignment to `t[i]`).

- **Literal:** parentheses `(1, 2, 3)` or just commas: `1, 2, 3`.
- **Single-element tuple** needs a trailing comma: `(42,)` — not `(42)`, which is just an integer in parentheses.
- **Unpacking:** `a, b = (1, 2)` assigns `a=1`, `b=2`.

**When to use tuples:** fixed records (x, y), function return of multiple values, dictionary keys (lists cannot be keys because they are mutable).

## Beginner-friendly notes

- Tuples are **lighter** and signal “this bundle should stay together and not be modified.”
- You can still **read** by index, **slice**, and **loop** over tuples like lists (e.g. `point[0:2]` is a new tuple with the first two items).
- For a “constant sequence” of settings or coordinates, prefer a tuple.

## Example

```python
point = (10, 20)
print(point[0], point[1])

x, y = point
print("x =", x, "y =", y)

single = (99,)
print(single, type(single))
```

## Expected output

```text
10 20
x = 10 y = 20
(99,) <class 'tuple'>
```

## Mini practice

1. Create a tuple `rgb = (255, 128, 0)` and print each channel on its own line using unpacking or indices.
2. Try to assign `rgb[0] = 0` and read the error message—then explain in one sentence why it failed.
3. Write a function-free line: `a, b, c = (1, 2, 3)` and print `a + b + c`.

Continue with `03-sets.md`.
