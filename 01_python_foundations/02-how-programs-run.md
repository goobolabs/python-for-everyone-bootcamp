# How Programs Run

## Theory

A **computer** executes very simple operations extremely fast. Most programmers never write those raw machine instructions by hand; they write **source code** in a language like Python. Another program—the **interpreter** or **compiler**—bridges the gap:

- With **Python**, the **interpreter** reads your source and executes it (often line by line in interactive mode, or from top to bottom in a script file).
- **Execution** means: fetch the next instruction, do what it says, update memory (variables), repeat.

Important ideas for beginners:

- **Order matters.** Code runs **sequentially** unless something (like an `if` in **Section 2**, or a **loop** in **Section 3**) changes the flow.
- **State** means “what values are stored now?” Variables remember values between lines.
- **Output** appears when your code **asks** for it (e.g. `print`) or writes to a file—not every line automatically shows on screen.

## Beginner-friendly notes

- Think **recipe**: step 1, step 2, step 3. If you skip a step, the result is wrong.
- The computer does not “know what you meant”—only what you wrote.
- **Save** your file before running a script; editors run the **saved** version.

## Example

Trace this mentally **before** you run it: first `score` is `10`, then it becomes `15`.

```python
score = 10
score = score + 5
print("score is", score)
```

## Expected output

```text
score is 15
```

## Mini practice

1. Change the `+ 5` to `+ 3` and predict the printed line before running.
2. Add a line **between** the two assignments: `print(score)`. Predict **two** lines of output (first line shows `10`, second line still `15` after the addition)—run and confirm.
3. In one sentence: why does **order of lines** matter here?

Continue with `03-pseudocode-and-flow-thinking.md`.
