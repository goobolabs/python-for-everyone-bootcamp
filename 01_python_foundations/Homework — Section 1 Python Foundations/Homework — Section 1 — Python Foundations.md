# Section 1: Python Foundations — Complete Study Guide

> **Who is this for?** Complete beginners. Every step is explained in plain language.
> No experience needed — just follow along one step at a time.

---

## Before You Start

### What is Python?
Python is a programming language. A programming language lets you give instructions to your computer. Python is one of the easiest to learn because it reads almost like plain English.

### What is a terminal?
A terminal is a window where you type commands directly to your computer. No clicking — just typing. It looks like a black or white box with a blinking cursor.

**How to open your terminal:**
- **Windows** — press the Windows key, type `cmd`, press Enter
- **Mac** — press `Cmd + Space`, type `Terminal`, press Enter

### What is a `.py` file?
A `.py` file is a Python file. It is a plain text file that contains Python code. You create it in a text editor (like Notepad) and run it in the terminal.

---

## Assignment 1: Environment Checklist

### What are you doing?
Proving that Python is installed on your computer and that you can run a file. Think of it like turning the ignition key before driving — you just need to confirm everything is working.

---

### Step 1 — Check your Python version

Open your terminal and type this, then press Enter:

```
python --version
```

You will see something like:

```
Python 3.11.4
```

That number is your **Python version**. Write it down — that is your answer for part 1.

> **If you see an error:** try `python3 --version` instead. One of the two will work depending on your operating system.

---

### Step 2 — Create your first Python file

Open Notepad (Windows) or TextEdit (Mac). Type exactly this:

```python
print("Hello, world!")
```

> **What does `print()` do?**
> It tells Python to show something on the screen. Whatever you put inside the brackets will appear in the terminal when you run the file.

Save the file as `hello.py` on your Desktop.

> **Important:** Make sure the file name ends in `.py` — not `.py.txt`. In Notepad, choose "All Files" in the save type dropdown before saving.

---

### Step 3 — Run the file from the terminal

In your terminal, navigate to your Desktop by typing:

```
cd Desktop
```

> **What does `cd` mean?** It stands for "change directory." It moves you into a folder — in this case, your Desktop folder.

Now run your file:

```
python hello.py
```

You should see:

```
Hello, world!
```

That means Python is working correctly.

---

### Step 4 — Write up your deliverable

Note down these three things:
1. Your Python version (e.g. `Python 3.11.4`)
2. The command you ran (e.g. `python hello.py`)
3. The output you saw (e.g. `Hello, world!`)

**The code for this assignment:**

```python
# hello.py
# This file proves Python is installed and working.

print("Hello, world!")
```

**Deliverable:** Short text or screenshot showing version + successful run.

---

---

## Assignment 2: Personal Intro Program

### What are you doing?
Writing a program that asks the user two questions, then prints a friendly message using their answers. This teaches you how to collect input from a user and use it in your output.

---

### Key concepts before you start

**What is a variable?**
A variable is like a labeled box. You put a value inside the box and give it a name. Later you can use that name to get the value back out.

```python
name = "Alikey"
# The box is called "name" and it holds the text "Alikey"
```

**What is `input()`?**
`input()` pauses the program and waits for the user to type something. Whatever the user types gets saved into a variable.

```python
name = input("What is your first name? ")
# Python shows the question, waits, then saves what the user types into "name"
```

**What is `+` used for with text?**
In Python, `+` can join two pieces of text together. This is called concatenation.

```python
print("Hello " + "Alikey")
# Output: Hello Alikey
```

---

### Step 1 — Create the file

Open your text editor and create a new file. Save it as `intro.py`.

---

### Step 2 — Write the code

Type this exactly into your file:

```python
# intro.py
# This program asks for a name and a color, then prints a friendly message.

name = input("What is your first name? ")
color = input("What is your favorite color? ")
print("Hello " + name + "! Your favorite color is " + color + ".")
```

---

### Step 3 — Understand each line

| Line | Code | What it does |
|------|------|-------------|
| 1–2 | `# ...` | Comments — Python ignores these, they are notes for you |
| 4 | `name = input(...)` | Shows the question, waits for the user to type, saves their answer into `name` |
| 5 | `color = input(...)` | Same thing but saves the answer into `color` |
| 6 | `print(...)` | Joins your text and both variables together and shows the result |

> **Why does order matter?**
> Python runs your code from top to bottom, one line at a time. If you tried to use `name` on line 3 before defining it on line 4, Python would not know what `name` is and would give you an error. **Order of lines always matters.**

---

### Step 4 — Run the file

In your terminal:

```
python intro.py
```

Type your answers when Python asks:

```
What is your first name? Alikey
What is your favorite color? blue
Hello Alikey! Your favorite color is blue.
```

**Deliverable:** `intro.py` + example run with sample input/output.

---

---

## Assignment 3: Types Practice

### What are you doing?
Learning that Python has different kinds of data called **types**. You will create one variable of each type and use a built-in tool called `type()` to confirm what each one is.

---

### Key concepts before you start

**The four basic types in Python:**

| Type name | What it stores | Example |
|-----------|---------------|---------|
| `int` | Whole numbers, no decimal | `25`, `0`, `-7` |
| `float` | Numbers with a decimal point | `98.6`, `3.14` |
| `str` | Text — short for "string" | `"Good morning"`, `"hello"` |
| `bool` | Only two possible values: `True` or `False` | `True`, `False` |

> **Why do types matter?**
> Python behaves differently depending on the type. For example, `2 + 3` gives `5` (adding two integers), but `"2" + "3"` gives `"23"` (joining two strings). Knowing the type helps you understand what Python will do with your data.

**What is `type()`?**
It is a built-in Python tool that tells you what type a value or variable is.

```python
type(25)          # returns <class 'int'>
type("hello")     # returns <class 'str'>
type(True)        # returns <class 'bool'>
```

---

### Step 1 — Create the file

Save a new file as `types_practice.py`.

---

### Step 2 — Write the code

```python
# types_practice.py
# This program creates one variable of each type and checks them with type().

# Create four variables — one of each type
age = 25
temperature = 98.6
greeting = "Good morning"
is_sunny = True

# Print each variable alongside its type
print(age, type(age))
print(temperature, type(temperature))
print(greeting, type(greeting))
print(is_sunny, type(is_sunny))

# One extra line combining string and boolean in a short message
print("Is it sunny?", is_sunny)
```

---

### Step 3 — Understand each line

| Line | Code | What it does |
|------|------|-------------|
| 5 | `age = 25` | Creates an integer variable called `age` |
| 6 | `temperature = 98.6` | Creates a float variable called `temperature` |
| 7 | `greeting = "Good morning"` | Creates a string variable called `greeting` |
| 8 | `is_sunny = True` | Creates a boolean variable called `is_sunny` |
| 11–14 | `print(x, type(x))` | Prints the value and then its type, separated by a space |
| 17 | `print("Is it sunny?", is_sunny)` | Prints a label and the boolean value together using a comma |

> **Why use commas in `print()` instead of `+`?**
> Commas work with any type. The `+` operator only joins strings — if you tried `"Is it sunny?" + True`, Python would give you an error because you cannot add text and a boolean directly. Commas are safer when mixing types.

---

### Step 4 — Run the file

```
python types_practice.py
```

**Expected output:**

```
25 <class 'int'>
98.6 <class 'float'>
Good morning <class 'str'>
True <class 'bool'>
Is it sunny? True
```

**Deliverable:** `types_practice.py` + pasted output.

---

---

## Assignment 4: Pseudocode Then Code

### What are you doing?
Learning to plan before you code. You write your steps in plain English first (called pseudocode), then translate those steps into Python. This is a real skill that professional programmers use every day.

---

### Key concepts before you start

**What is pseudocode?**
Pseudocode is a plain-language description of what your program will do. There are no Python rules — just your own words. Think of it like writing a recipe before you cook.

```
Example pseudocode:
Step 1: Store a person's name
Step 2: Store the city they live in
Step 3: Print a sentence using the name
Step 4: Print a sentence using the city
```

**What is a comment in Python?**
A comment starts with `#`. Python completely ignores everything after `#` on that line. Comments are notes for humans reading the code — they help explain what is happening and why.

```python
# This is a comment — Python skips this line entirely
print("But Python does run this line")
```

> **Why write pseudocode first?**
> It lets you think through the logic before worrying about Python's exact rules. Many bugs happen because people start typing code before they have a clear plan. Pseudocode is your plan.

---

### Step 1 — Plan your pseudocode

Choose two pieces of text. For this example we will use a name and a city. Write your steps in plain English:

```
Step 1: Store a person's name
Step 2: Store the city they live in
Step 3: Print a sentence using the name
Step 4: Print a sentence using the city
```

---

### Step 2 — Create the file

Save a new file as `pseudocode_practice.py`.

---

### Step 3 — Write pseudocode as comments at the top

```python
# pseudocode_practice.py

# --- PSEUDOCODE ---
# Step 1: Store a person's name
# Step 2: Store the city they live in
# Step 3: Print a sentence using the name
# Step 4: Print a sentence using the city
```

---

### Step 4 — Write the Python code below your comments

```python
# pseudocode_practice.py

# --- PSEUDOCODE ---
# Step 1: Store a person's name
# Step 2: Store the city they live in
# Step 3: Print a sentence using the name
# Step 4: Print a sentence using the city

# --- PYTHON CODE ---

# Step 1 and 2: Store two pieces of text in variables
person = "Ali Omar"
city = "Mogadishu"

# Step 3: Print a sentence using the name
print("The person's name is " + person + ".")

# Step 4: Print a sentence using the city
print("They live in " + city + ".")
```

---

### Step 5 — Understand each line

| Line | Code | What it does |
|------|------|-------------|
| `person = "Alikey"` | Creates a string variable called `person` holding the text `"Alikey"` |
| `city = "Mogadishu"` | Creates a string variable called `city` holding `"Mogadishu"` |
| `print("The person's name is " + person + ".")` | Joins three pieces of text and prints the result |
| `print("They live in " + city + ".")` | Does the same for the second sentence |

---

### Step 6 — Run the file

```
python pseudocode_practice.py
```

**Expected output:**

```
The person's name is Alikey.
They live in Mogadishu.
```

**Deliverable:** `pseudocode_practice.py` with pseudocode comments at the top + code below + pasted output.

---

---

## Assignment 5: Short Reflection (Optional)

Write 5–8 sentences answering these three questions:

1. **What was easiest** and **what was hardest** in Section 1?
2. **Name one error** you saw while debugging and how you fixed it — or how you would fix it next time.
3. **What will you review** before starting Section 2?

> **Tip:** There is no wrong answer here. The goal is to reflect on what you learned. Even writing "I struggled with X but fixed it by doing Y" shows real understanding.

---

---

## All Four Files — Quick Reference

Here is every file you need to submit, all in one place.

---

### `hello.py`

```python
# hello.py
# Assignment 1: proves Python is installed and working.

print("Hello, world!")
```

---

### `intro.py`

```python
# intro.py
# Assignment 2: asks for a name and color, prints a friendly message.

name = input("What is your first name? ")
color = input("What is your favorite color? ")
print("Hello " + name + "! Your favorite color is " + color + ".")
```

---

### `types_practice.py`

```python
# types_practice.py
# Assignment 3: creates one variable of each type and checks them with type().

# Four variables — one of each type
age = 25
temperature = 98.6
greeting = "Good morning"
is_sunny = True

# Print each variable and its type
print(age, type(age))
print(temperature, type(temperature))
print(greeting, type(greeting))
print(is_sunny, type(is_sunny))

# One extra line using string and boolean together
print("Is it sunny?", is_sunny)
```

---

### `pseudocode_practice.py`

```python
# pseudocode_practice.py
# Assignment 4: pseudocode plan followed by Python implementation.

# --- PSEUDOCODE ---
# Step 1: Store a person's name
# Step 2: Store the city they live in
# Step 3: Print a sentence using the name
# Step 4: Print a sentence using the city

# --- PYTHON CODE ---
person = "Alikey"
city = "Mogadishu"

print("The person's name is " + person + ".")
print("They live in " + city + ".")
```

---

---

## Grading Checklist (Self-Check)

Go through this list before you submit. If you can tick every box, you are ready.

- [ ] All scripts run without errors.
- [ ] Variable names are readable and make sense (e.g. `age` not `x`).
- [ ] Output matches what the program is supposed to print.
- [ ] Comments explain *why* where it helps — not every single line.
- [ ] You can explain in one sentence how **order of lines** affects output.

> **One sentence answer for the last point:** Python runs code from top to bottom, so if you use a variable before you create it, Python will not know what it is and will give you an error.

---

