# Dataclasses

## Theory

Many classes only **store fields** and need **`__init__`**, **`__repr__`**, maybe **`__eq__`**—that’s repetitive. Python’s **`dataclasses`** module (**Python 3.7+**) generates boilerplate for you:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    active: bool = True
```

This creates **`__init__`**, **`__repr__`**, and comparisons helpers automatically. You still add **methods** on the class as usual.

## Beginner-friendly notes

- Requires **`from dataclasses import dataclass`** once per file (or import the decorator however your style guide says).
- Type hints (**`str`**, **`bool`**) are **annotations**—they help readers and tools; Python does **not** enforce them at runtime by default.
- Defaults (**`= True`**) must come **after** fields without defaults.

## Example

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
q = Point(1, 2)
print(p)
print(p == q)
```

## Expected output

```text
Point(x=1, y=2)
True
```

## Mini practice

1. Rewrite **`Book`** (title, author, pages) as a **`@dataclass`** and **`print`** two equal books—confirm **`==`** works as expected.
2. Give **`pages`** a default of **`0`**.
3. Add a method **`short_title(self)`** that returns the first **10** characters of **`title`**—methods work on dataclasses too.

Continue with `07-composition.md`.
