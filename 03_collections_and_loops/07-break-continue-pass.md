# `break`, `continue`, and `pass`

## Theory

These keywords change flow inside **loops** (`for` or `while`):

- **`break`** — Stops the **innermost** loop you are in and jumps to the code **after** the loop.
- **`continue`** — Skips the **rest of this iteration** and goes to the **next** check / next item.
- **`pass`** — A **no-op** placeholder: does nothing. The line is only there so Python’s syntax is valid (e.g. empty `if` or a stub you will fill later). It is **not** a loop “skip” like `continue`.

## Beginner-friendly notes

- `break` helps “find and stop” and simple **menu exits**.
- `continue` helps “skip bad lines” (e.g. empty input) without nesting everything in `else`.
- If you have many `break`/`continue` in one loop, an **`if`/`else` layout** is sometimes easier to read—your choice as you get comfortable.

## Example

```python
# break: stop early
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        print("stopping at 4")
        break
    print(n)

# continue: skip even
for n in range(6):
    if n % 2 == 0:
        continue
    print("odd:", n)
```

## Expected output

```text
1
2
3
stopping at 4
odd: 1
odd: 3
odd: 5
```

## Mini practice

1. Loop **`for n in range(20)`** and **`break`** right after you **`print(5)`** (or stop when `n` reaches 5), so you do not print past that point—experiment with the condition.
2. Loop over **`range(10)`**; if `n` is **3**, use **`continue`** so you skip printing for that `n` only.
3. Write an **`if False:`** block whose only statement is **`pass`**, to show the file still runs.

Continue with `08-common-methods.md`.
