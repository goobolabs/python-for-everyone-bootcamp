# Instance methods

## Theory

**Instance methods** are functions **defined inside** a class that take **`self`** as the first parameter. They **belong to** each object: when you call **`obj.method(...)`**, Python passes **`obj`** as **`self`**.

Use methods for **behavior** that uses or updates the object’s attributes.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def bump(self):
        self.count += 1

c = Counter()
c.bump()
print(c.count)
```

Same idea as functions you already know—the only new rule is **`self`** and the **indentation** under **`class`**.

## Beginner-friendly notes

- **`self`** is a **convention** (you could name it `this`, but don’t—everyone expects **`self`**).
- Methods can **`return`** values like ordinary functions.
- Call methods **after** you have an instance: **`c.bump()`**, not **`Counter.bump()`** without an instance (class methods come later in other courses).

## Example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print(r.area())
```

## Expected output

```text
20
```

## Mini practice

1. Add **`def perimeter(self):`** to **`Rectangle`** that returns **`2 * (self.width + self.height)`**.
2. Define **`class BankAccount`** with **`balance`** starting at **`0`** and a method **`deposit(self, amount)`** that adds **`amount`** to **`balance`** (assume **`amount`** is positive for now).
3. Call **`deposit`** twice on one account and **`print`** the **`balance`**.

Continue with `03-class-and-instance-attributes.md`.
