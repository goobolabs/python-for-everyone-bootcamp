# Class and instance attributes

## Theory

- **Instance attributes** are set on **`self`** (usually in **`__init__`**): **each object** has its **own** copy (`self.name`, `self.balance`).
- **Class attributes** are assigned **on the class** (outside **`__init__`**, at class body level). **All instances share** the **same** class attribute unless you **shadow** it by setting **`self.attr`** on one instance.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

a = Dog("Ada")
b = Dog("Bo")
print(a.species, b.species)
print(a.name, b.name)
```

**Pitfall:** Do **not** use a **mutable** default shared by all instances as a **class** attribute if each instance needs its **own** list—use **`self.items = []`** inside **`__init__`**, not **`items = []`** at class level (unless you truly want sharing).

## Beginner-friendly notes

- Read **`obj.attr`**: Python looks on the **instance** first, then the **class**.
- Use class attributes for **constants** or **shared counters** you understand fully; when unsure, put data on **`self`**.

## Example

```python
class Ticket:
    next_id = 1

    def __init__(self, event):
        self.id = Ticket.next_id
        self.event = event
        Ticket.next_id += 1

t1 = Ticket("PyCon")
t2 = Ticket("Meetup")
print(t1.id, t2.id)
```

## Expected output

```text
1 2
```

## Mini practice

1. Add **`species`** as a **class** attribute on **`Dog`** from the theory snippet and print it for two dogs.
2. Explain in one sentence why **`self.names = []`** in **`__init__`** is safer than **`names = []`** on the class when every student needs their **own** grade list.
3. (Stretch) Create **`Counter`** with a **class** attribute **`total_created`** incremented in **`__init__`**; print **`total_created`** after creating three instances.

Continue with `04-str-and-repr.md`.
