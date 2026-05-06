# Scope

## Theory

**Scope** answers: “where is this name visible?”

- **Local:** names assigned **inside** a function are local to that function (unless declared otherwise).
- **Global:** names defined at **module level** (top of `.py` file) are visible inside functions for **reading**; assignment creates a **local** name unless you use **`global`** or **`nonlocal`**.

**LEGB rule** (search order): **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

Beginners should **minimize** `global`; prefer passing values in and returning results.

## Beginner-friendly notes

- `x = 1` inside a function creates a **local** `x` even if a global `x` exists—unless you said `global x`.
- **Loops** and **`if`** do not create a new scope in Python (only functions, classes, modules, comprehensions in a sense—details later).

## Example

```python
count = 0  # global

def bump():
    global count
    count += 1

bump()
bump()
print(count)

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())
```

## Expected output

```text
2
11
```

## Mini practice

1. Predict output of:

```python
total = 100
def demo():
    total = 5
    print(total)
demo()
print(total)
```

Run and explain **two** `total`s.

2. Refactor a script that uses `global` to avoid globals by **returning** the new value instead (conceptual exercise).

Continue with `homework.md`.
