# Installation

## Theory

To run Python on your computer, you need a **Python interpreter** installed. Most learners use the official installer from [python.org](https://www.python.org/downloads/) or a version provided by their operating system package manager.

**Important:** On many systems, the command is `python3` (Python 3) and `python` might point to an older version or not exist. Always check with `python3 --version` or `python --version`.

**Virtual environments** (optional for this section): later you may use `venv` to keep project dependencies separate. For Section 1, a single system-wide or user install is enough to practice.

## Beginner-friendly notes

- **Do not panic** if install steps differ slightly by OS; follow one reliable guide and verify with `--version`.
- On **Windows**, check “Add Python to PATH” during install if the installer offers it.
- On **macOS/Linux**, you may use `python3` explicitly in the terminal.
- Use a **text editor** or **IDE** you like (VS Code, Cursor, PyCharm, etc.); Python itself does not require a specific editor.

## Example (verify install)

After installing, open a terminal and run:

```bash
python3 --version
```

Or on some Windows setups:

```bash
python --version
```

Then start the interactive interpreter:

```bash
python3
```

Type:

```python
print("Install OK")
```

Exit the interactive session with `exit()` or **Ctrl+D** (Linux/macOS) / **Ctrl+Z** then Enter (some Windows setups).

## Expected output

Version command (example—your version number may differ):

```text
Python 3.12.1
```

Interactive `print`:

```text
Install OK
```

## Mini practice

1. Run `python3 --version` (or `python --version`) and write down the exact version string.
2. Open interactive Python and print your name. Confirm you see your name.

Continue with `06-running-scripts.md`.
