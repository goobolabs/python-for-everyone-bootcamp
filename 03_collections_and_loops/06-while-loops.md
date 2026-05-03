# `while` loops

## Theory

A **`while`** loop repeats a block **as long as a condition is true**:

```python
while condition:
    # indented block
```

The condition is checked **before** each iteration. If it is false at the start, the body runs **zero** times.

**When to use `while`:** the number of iterations is not known up front, or the loop is driven by user input, sensor-like checks, or “keep going until something happens.” When you are walking a **list** you already have, a **`for`** loop is usually clearer. **`while`** pairs well with **counters** you update yourself, **menus** (“repeat until user quits”), and **validation** (“ask until the input is valid”).

**Infinite loops:** if the condition never becomes false, the loop never stops. Always ensure something inside the loop can make the condition false, or you **`break`** out (next lesson).

## Beginner-friendly notes

- `while True:` plus a **`break`** is a common pattern for “loop until a clear exit.”
- Compare to **`for`**: `for` = “over this data”; `while` = “until this condition flips.”
- Watch **`Indentation`**: the whole body must be indented; changing a counter in the wrong place is a common bug.

## Example

```python
# count up
n = 1
while n <= 3:
    print("n is", n)
    n = n + 1

# guard with input (simple)
line = ""
while line != "done":
    line = input("type a word, or 'done' to stop: ")
    if line != "done":
        print("you said:", line)
print("ok, bye")
```

(When you run the second example, type `done` to stop.)

## Expected output (first example)

```text
n is 1
n is 2
n is 3
```

## Mini practice

1. Set `i = 0`. Use **`while i < 4`**: print `i`, then add **1** to `i` each time.
2. **Stretch:** set `total = 0` and add numbers from user input in a `while` loop until they type **`0`**, then print `total`. (If that is much harder, skip and ask a peer.)

Continue with `07-break-continue-pass.md`.
