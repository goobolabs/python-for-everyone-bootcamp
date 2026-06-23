# Classes and objects

## Theory

Programs often need to group **related data** with **operations on that data**. In Python you define a **blueprint** called a **class**, then create **instances** (**objects**) from it.

- **`class Name:`** introduces the type.
- **`__init__(self, ...)`** runs when you **construct** an instance; **`self`** refers to **that** instance.
- **Attributes** hang off the instance: `self.value = ...` inside methods; outside you use `obj.value`.

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

c = Counter(10)
print(c.count)
```

Think of **`self`** as “this object”—Python passes the instance as the first argument automatically when you call `c.method(...)`.

## Beginner-friendly notes

- Class names often use **`CapWords`** (e.g. `BankAccount`), unlike **`snake_case`** functions.
- **`__init__`** is not a constructor in the C++ sense; it **initializes** the instance after it exists.
- One file can hold several classes; start with **one** class per exercise.

## Example

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 3)
print(buddy.name, buddy.age)
```

## Expected output

```text
Buddy 3
```

## Mini practice

1. Define **`class Book`** with **`__init__(self, title, author)`** and store **`title`** and **`author`** on **`self`**. Create two **`Book`** instances and print each **`title`**.
2. Add an integer **`pages`** to **`Book`** and set it in **`__init__`**. Print **`pages`** for one book.
3. In one sentence: what is the difference between **`class Book`** and **`b = Book(...)`**?

Continue with `02-instance-methods.md`.
