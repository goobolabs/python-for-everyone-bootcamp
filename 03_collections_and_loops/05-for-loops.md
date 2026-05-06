# `for` loops (collections, `range`, and common patterns)

## Part 1 — Basic `for` and `range`

A **`for`** loop runs a block **once for each item** in an **iterable**—something you can step through: a **list**, **string**, **`range`**, dict keys, and more.

```python
for name in items:
    # block runs per item
```

On each step, the loop variable is bound to the **next** value. When the iterable is exhausted, the loop ends.

**`range`:** builds a simple sequence of integers to count with `for`, without building a full list in memory (Python 3: `range` is lazy).

| Call | Meaning |
|------|---------|
| `range(stop)` | `0` … `stop - 1` |
| `range(start, stop)` | `start` … `stop - 1` |
| `range(start, stop, step)` | same, with a step (can be negative) |

**Stop is exclusive** (like slices): `range(3)` is `0`, `1`, `2`.

### Beginner-friendly notes (basics)

- Pick a **clear** loop variable: `for score in scores`, not only `i` unless you mean an index.
- **Strings** are iterables: `for ch in word` visits each character.
- `for i in range(len(items))` works but is often clunkier than `for x in items` or **`enumerate`** (below).

### Example (basics)

```python
# list
colors = ["red", "blue", "green"]
for c in colors:
    print("color:", c)

# string
for ch in "Hi!":
    print(ch)

# range: repeat or count
for n in range(3):
    print("n =", n)

for n in range(1, 5):
    print(n)
```

### Expected output (basics)

```text
color: red
color: blue
color: green
H
i
!
n = 0
n = 1
n = 2
1
2
3
4
```

---

## Part 2 — `enumerate`, dictionaries, unpacking

Same **`for`** keyword—here are **patterns** you use often in real code.

- **Index + value:** avoid `for i in range(len(items)):` when you can use **`enumerate(items)`** → `for i, x in enumerate(items):`
- **Dictionary — keys (default):** `for k in d:` (same as `d.keys()` for iteration)
- **Values:** `for v in d.values():`
- **Key + value:** `for k, v in d.items():`
- **Unpacking** in the header: `for a, b in pairs:` when each item is a two-tuple (or two values to unpack)

### Beginner-friendly notes (patterns)

- **Set** iteration: order is **arbitrary**—do not depend on order.
- **`enumerate`** starts at `0` by default; `enumerate(items, start=1)` for 1-based line numbers.
- Nested loops (loop inside loop) are fine; use clear names (`row`, `col`).

### Example (patterns)

```python
names = ["Ana", "Bo", "Cy"]
for i, name in enumerate(names):
    print(i, name)

scores = {"Ana": 90, "Bo": 88}
for name in scores:
    print(name, scores[name])

for name, score in scores.items():
    print(str(name) + ": " + str(score))
```

### Expected output (patterns)

```text
0 Ana
1 Bo
2 Cy
Ana 90
Bo 88
Ana: 90
Bo: 88
```

(Later you may use **f-strings** to format those lines more neatly.)

---

## Mini practice

1. Create `nums = [2, 4, 6]`. Use **`for`** to print each number doubled.
2. Use **`for n in range(5, 10):`** to print **5** through **9** on separate lines.
3. Ask for a **word** with `input()`. Use **`for`** to print every character on its own line.
4. Use **`enumerate`** on a list of three names; print the index and name on each line.
5. Build a small **dict** (e.g. two keys). Loop with **`.items()`** and print each key and value. Optional: print **sorted** keys with `for k in sorted(d):`.

Continue with `06-while-loops.md`.
