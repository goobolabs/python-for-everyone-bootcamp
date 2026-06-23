# Reading files

## Theory

Use **`open(path, mode, encoding=...)`** to work with files. For **reading text**, common choices:

- Mode **`"r"`** (default): read text.
- Always specify **`encoding="utf-8"`** for text files when possible—avoids surprises on different operating systems.

**Patterns:**

1. **Read whole file:** `data = f.read()`
2. **Read line by line:** `for line in f:` (memory-friendly for large files)
3. **Read all lines:** `lines = f.readlines()`

**Context manager** (best practice):

```python
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

This **closes** the file automatically, even if an error occurs.

## Beginner-friendly notes

- Paths can be relative to the **current working directory** when you run the script—students often trip here; print `Path.cwd()` from `pathlib` if confused.
- Text files often end lines with `\n`; `line.rstrip("\n")` removes newline for clean printing.

## Example

Assume a file `sample.txt` exists with two lines:

```text
Hello
World
```

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(repr(content))
```

## Expected output

```text
'Hello\nWorld\n'
```

(If the file is missing, you get `FileNotFoundError`—you will handle that in `04-try-except-finally.md`.)

## Mini practice

1. Create `sample.txt` with three lines yourself, then print the file **line by line** with a `for` loop.
2. Read the whole file into one string and print **how many** characters it has.
3. (Stretch) Read about `Path.read_text()` in `pathlib` and rewrite the read in one line.

Continue with `02-writing-files.md`.
