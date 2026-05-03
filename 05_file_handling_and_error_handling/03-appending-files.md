# Appending files

## Theory

Mode **`"a"`** opens a file for **append**: new writes go to the **end** without wiping existing content. If the file does not exist, it is **created**.

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("another line\n")
```

**Use cases:** logs, journals, incremental exports.

**Mixing modes:** `"r+"` read/write, `"w+"` truncate then read/write—advanced; stick to `r`, `w`, `a` first.

## Beginner-friendly notes

- If you open `"w"` by mistake, you **lose** old data—double-check the mode in code reviews.
- For concurrent writers (many processes), you need bigger tools; for class, single-process append is enough.

## Example

```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("start\n")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("more\n")

with open("log.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

## Expected output

```text
start
more

```

## Mini practice

1. Append your name to `log.txt` **twice** in one script (two `with` blocks or one block with two writes—your choice).
2. Print the full file after appending.
3. Explain in one sentence when you choose **`w`** vs **`a`**.

Continue with `04-try-except-finally.md`.
