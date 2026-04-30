# Writing files

## Theory

Open with mode **`"w"`** to **write** text. If the file exists, it is **truncated** (overwritten) by default.

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")
```

Use **`write`** for strings you build yourself; `print(..., file=f)` is also common.

**Important:** `"w"` destroys previous content. If you meant to add to the end, use **`"a"`** (append—see `03-appending-files.md`).

## Beginner-friendly notes

- Create parent directories before writing deep paths, or use `Path.mkdir(parents=True)`.
- Always use `encoding="utf-8"` for text unless you have a reason not to.

## Example

```python
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

## Expected output

```text
Hello, file!

```

## Mini practice

1. Write a file `greeting.txt` with your name on line 1 and today’s date as plain text on line 2 (type the date manually is fine).
2. Run the script twice—confirm the file still has **only** what your last run wrote (overwrite behavior).
3. Delete `hello.txt` / `greeting.txt` when done if you do not want clutter (optional).

Continue with `03-appending-files.md`.
