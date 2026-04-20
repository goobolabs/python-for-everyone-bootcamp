# Running scripts

## Theory

You can run Python in two common ways:

1. **Interactive mode (REPL)** — You type commands one at a time; Python runs each line immediately. Great for quick experiments.
2. **Script mode** — You put code in a **text file** with a `.py` extension and run the whole file. This is how real programs are usually stored and shared.

The **REPL** (“Read–Eval–Print Loop”) reads input, evaluates it, prints the result, and loops. A **script** runs from top to bottom when you start it.

## Beginner-friendly notes

- Save scripts as **plain text**, not Word `.docx` format.
- File name: use letters, numbers, underscores; avoid spaces if possible (e.g. `hello.py` not `my program.py`).
- From the terminal, your current folder matters: you either `cd` to the script’s directory or pass the full path.

## Example: script file

You already used `print(...)` in the installation lesson (interactive mode). A script is the same idea: those lines saved in a file—no variables or math needed yet.

Create a file named `hello.py` with this content (put **your** name inside the quotes):

```python
print("Hello!")
print("My name is Sam.")
```

Run it from the same directory as the file:

```bash
python3 hello.py
```

(On Windows you might use `python hello.py`.)

## Expected output

If you used the text above, you should see something like:

```text
Hello!
My name is Sam.
```

## Mini practice

1. Create `greet.py` that prints two lines: your name and one hobby.
2. Run it from the terminal using `python3 greet.py` (or `python greet.py`).
3. Change one line, save, and run again—build the habit: **edit → save → run**.

Continue with `07-variables.md`.
