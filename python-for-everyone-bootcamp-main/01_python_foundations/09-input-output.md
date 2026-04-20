# Input and output

## Theory

- **`print(...)`** sends text to the “standard output” (usually your terminal). You can print several items separated by commas; `print` adds spaces between them and adds a **newline** at the end by default.
- **`input(prompt)`** waits for the user to type a line and press Enter. It always returns a **string** (`str`), even if the user types digits.

If you need a number from the user, you **convert** the string:

- `int(...)` for integers
- `float(...)` for decimal numbers

## Beginner-friendly notes

- Always read `input()` as text first, then convert—this avoids surprises.
- If conversion fails (e.g. `int("hello")`), Python raises an error; you will learn to handle errors in a later section.
- `print` can take a `sep` and `end` argument later; for now, default behavior is enough.

## Example

```python
name = input("What is your name? ")
age_text = input("How old are you? ")
age = int(age_text)

print("Hello,", name)
print("Next year you will be", age + 1)
```

**Sample interaction** (user types `Sam` and `18`):

## Expected output

```text
What is your name? Sam
How old are you? 18
Hello, Sam
Next year you will be 19
```

(The first two lines include what the user typed after the prompts.)

## Mini practice

1. Write a program that asks for two **integers** (two `input` calls, two `int(...)` conversions) and prints their sum.
2. Ask for a **float** price with `float(input(...))` and print the price with a label, e.g. `Price: 9.5`.

Continue with `10-comments.md`.
