# Inheritance

## Theory

**Inheritance** lets one class **reuse** and **extend** another: **`class Child(Parent):`** means **`Child`** **is-a** **`Parent`** for purposes of shared behavior.

- **`Child`** inherits methods from **`Parent`** unless **overridden** (same method name, new body in **`Child`**).
- **`super()`** refers to the **parent** class—common pattern in **`__init__`** so both parent and child set up fields:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "woof"
```

Stick to **single inheritance** in this course—one parent per class.

## Beginner-friendly notes

- Only factor out a parent when several classes truly **share** behavior; otherwise **composition** (next lessons) is often clearer.
- **`super().__init__(...)`** must receive whatever **`Animal.__init__`** expects.

## Example

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}"

class FormalGreeter(Greeter):
    def hello(self):
        return f"Good day, {self.name}."

f = FormalGreeter("Sam")
print(f.hello())
```

## Expected output

```text
Good day, Sam.
```

## Mini practice

1. Define **`Rectangle`** with **`width`**, **`height`**, and **`area(self)`**. Define **`Square(Rectangle)`** whose **`__init__`** takes **`side`** and calls **`super().__init__(side, side)`**.
2. Override **`__str__`** in **`Square`** to say **`Square(side=...)`**.
3. Predict **`Square(5).area()`** before you run it.

Continue with `06-dataclasses.md`.
