# Default arguments

## Theory

You can give parameters **defaults** so callers may omit them:

```python
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)
```

**Rules:** parameters with defaults must come **after** parameters without defaults.

**Mutable default pitfall:** do **not** use mutable objects as defaults unless you mean to share state:

```python
# BAD for beginners
def add_item(x, items=[]):
    items.append(x)
    return items
```

Each call can accidentally reuse the **same** list object. Prefer `None` and create a new list inside the function.

## Beginner-friendly notes

- Defaults make APIs convenient: `open(path, mode="r")`-style patterns.
- If unsure, default to **`None`** and build fresh objects in the body.

## Example

```python
def repeat(word, times=2):
    return (word + " ") * times

print(repeat("hi"))
print(repeat("go", 3))
```

## Expected output

```text
hi hi 
go go go 
```

## Mini practice

1. Write `def divider(a, b=1):` that returns `a / b`. Call it with one argument and with two.
2. Explain why `def bad(x, items=[])` can surprise you; then write a **safe** version using `items=None`.

Continue with `05-args-and-kwargs.md`.
