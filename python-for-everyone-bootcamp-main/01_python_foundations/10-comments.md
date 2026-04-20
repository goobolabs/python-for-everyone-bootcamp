# Comments

## Theory

A **comment** is text in your source code that Python **ignores** when running the program. Comments exist for **humans**: future you, teammates, or teachers reading your code.

In Python:

- **`#` starts a comment** that runs to the end of the line.
- There is no “block comment” syntax like `/* ... */` in some languages; multi-line explanations use multiple `#` lines or a **docstring** (a string literal used as documentation—more in later sections).

Use comments to explain **why** something is done or to clarify tricky logic—not to repeat what the code obviously says.

## Beginner-friendly notes

- Good: `# Convert user text to integer for math`
- Less helpful: `# Set x to 5` right above `x = 5`
- Comments can go **after** code on the same line: `pi = 3.14  # approximation`

## Example

```python
# Program: show a simple calculation
width = 10
height = 4
area = width * height  # rectangle area

print("Area:", area)
# print("Debug:", width, height)  # uncomment temporarily to debug
```

## Expected output

```text
Area: 40
```

## Mini practice

1. Take a short program you wrote earlier (e.g. from `06-running-scripts.md`). Add one comment explaining the **purpose** of the script at the top.
2. Add an inline comment next to one variable explaining **units** (e.g. `# centimeters` or `# dollars`).

Continue with `11-debugging-mindset.md`.
