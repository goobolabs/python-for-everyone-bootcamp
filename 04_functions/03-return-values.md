# Return values

## Theory

**`return`** ends the function call and sends a value back to the caller:

```python
def double(x):
    return x * 2
```

If you omit `return` or use bare `return`, Python returns **`None`** (a singleton meaning “nothing useful”).

**Multiple values:** `return a, b` actually returns **one tuple** `(a, b)`—you can unpack: `x, y = f()`.

## Beginner-friendly notes

- Code after `return` in the same block does not run (“dead code”).
- Use `return` when the function **computes** something; use bare `print` only when the function’s job is truly to display.

## Example

```python
def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

def stats(a, b):
    return a + b, a * b

print(clamp(15, 0, 10))
print(stats(3, 4))
```

## Expected output

```text
10
(7, 12)
```

## Mini practice

1. Write `def is_even(n):` that returns `True` or `False` (use `%`).
2. Write `def max_of_two(a, b):` that returns the larger value (no `max()`—use `if` for practice).
3. Call `stats(3, 4)`, assign to two variables with unpacking, and print them.

Continue with `04-default-arguments.md`.
