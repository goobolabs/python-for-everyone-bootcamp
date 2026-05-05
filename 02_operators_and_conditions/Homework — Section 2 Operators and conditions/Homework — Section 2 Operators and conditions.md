# Python Homework — Section 2
### Operators and Conditions. Read slowly. Do one step at a time.

## Author: [Ali Omar](https://github.com/fernandodominguez)

---

## Before You Start — New Things in This Section

This section introduces new ideas. Read these first before touching any code.

---

### What is an `if` statement?

An `if` statement lets your program make a decision.
It checks if something is true, and only runs a block of code if it is.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Output:
```
You are an adult
```

> The code inside the `if` block is **indented** (pushed to the right with spaces or a Tab).
> Python uses indentation to know which lines belong to the `if` block.
> **Indentation is not optional — it is required.**

---

### What is `elif` and `else`?

- `elif` means "otherwise, if this other thing is true"
- `else` means "otherwise, for everything else"

```python
temperature = 10

if temperature >= 25:
    print("warm")
elif temperature >= 15:
    print("ok")
else:
    print("cold")
```

Python checks from top to bottom. The first condition that is true runs. The rest are skipped.

---

### What is `==`?

`==` checks if two things are equal. It asks "are these the same?"

```python
name = "Sara"

if name == "Sara":      # are they equal? yes
    print("Hello Sara")
```

> **Common mistake:** Do not confuse `=` and `==`
> - `=` means **give this variable a value** → `name = "Sara"`
> - `==` means **are these equal?** → `name == "Sara"`
> Using `=` inside an `if` condition is a very common error. Always use `==` for comparisons.

---

### What is `and` / `or`?

`and` and `or` let you combine two conditions into one check.

| Word | Meaning | True when |
|------|---------|-----------|
| `and` | both must be true | condition A **and** condition B are both true |
| `or` | at least one must be true | condition A **or** condition B is true |

```python
age = 16
has_ticket = True

if age >= 18 or has_ticket == True:
    print("You can enter")
```

> Use **parentheses `()`** when mixing `and` and `or` together.
> They make the rule easier to read and make sure Python follows the right order.

---

### What is `int(...)`?

`input()` always gives you text — even if the user types a number.
`int()` converts that text into a real integer so you can do math or comparisons with it.

```python
age = int(input("How old are you? "))
```

Without `int()`, the value would be text like `"20"` and you could not compare it to a number like `18`.

---
---

# Assignment 1 — Temperature Checker

**What you are doing:**
Asking the user for a temperature number, then telling them if it is warm, ok, or cold.

---

### Step 1 — Create the file

Save a new file as `temperature_input.py`.

---

### Step 2 — Write the code

```python
# temperature_input.py
# Asks the user for a temperature and tells them if it is warm, ok, or cold.

# Ask the user for a number and convert it to an integer
temperature = int(input("Enter a temperature: "))

# Check the temperature and print the right message
if temperature >= 25:
    print("warm")
elif temperature >= 15:
    print("ok")
else:
    print("cold")
```

---

### Step 3 — What each line does

```
temperature = int(input(...))  → asks the user to type a number,
                                  converts it from text to an integer,
                                  saves it into a variable called temperature

if temperature >= 25:          → is the temperature 25 or higher? if yes → print "warm"
elif temperature >= 15:        → if not, is it 15 or higher? if yes → print "ok"
else:                          → if neither of the above → print "cold"
```

> **Why does the order matter?**
> Python checks from top to bottom. If the temperature is 30, it matches `>= 25` first
> and prints "warm" — it never even looks at the `elif` or `else`.
> If you put `elif temperature >= 15` first, a temperature of 30 would print "ok" instead — which is wrong.
> **Order always matters in if/elif/else.**

---

### Step 4 — Run the file

```
python temperature_input.py
```

**Example run 1:**
```
Enter a temperature: 30
warm
```

**Example run 2:**
```
Enter a temperature: 18
ok
```

**Example run 3:**
```
Enter a temperature: 5
cold
```

---

### What to hand in:
`temperature_input.py` + paste one example run with any number you choose.

---
---

# Assignment 2 — Admin Gate (Nested Conditions)

**What you are doing:**
Writing a login system. First check the username. If the username is correct, then check the password.
A check inside another check is called a **nested condition**.

---

### Before you start — What is a nested condition?

A nested condition is an `if` statement inside another `if` statement.

```python
if username == "admin":
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

Think of it like two doors:
- **Door 1** — is the username correct? If no, stop here.
- **Door 2** — only asked if Door 1 opened. Is the password correct?

---

### Step 1 — Create the file

Save a new file as `admin_gate.py`.

---

### Step 2 — Write the code

```python
# admin_gate.py
# A simple login system that checks username then password.

# Step 1: Ask for the username
username = input("Enter your username: ")

# Step 2: Check if the username is "admin"
if username == "admin":

    # Step 3: Only ask for password if the username is correct
    password = input("Enter your password: ")

    # Step 4: Check if the password is correct
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")

else:
    # Username was not "admin" — stop here, do not ask for password
    print("Unknown user")
```

---

### Step 3 — What each line does

```
username = input(...)       → saves what the user types into "username"

if username == "admin":     → is the username exactly "admin"? (capital letters matter!)
    password = input(...)   → only runs if username is "admin" — asks for password
    if password == "secret":→ is the password exactly "secret"?
        print("Access granted")  → both username and password are correct
    else:
        print("Wrong password")  → username was right but password was wrong
else:
    print("Unknown user")   → username was not "admin" — program stops here
```

> **Important:** The indentation (spaces at the start of lines) tells Python which block
> each line belongs to. If your indentation is wrong, the program will not work correctly.
> Use 4 spaces (or one Tab) for each level.

---

### Step 4 — Run the file

```
python admin_gate.py
```

**Example run 1 — Access granted:**
```
Enter your username: admin
Enter your password: secret
Access granted
```

**Example run 2 — Wrong password:**
```
Enter your username: admin
Enter your password: hello
Wrong password
```

**Example run 3 — Unknown user:**
```
Enter your username: sara
Unknown user
```

---

### What to hand in:
`admin_gate.py` + paste two example runs — one that shows `"Access granted"` and one that shows `"Unknown user"` or `"Wrong password"`.

---
---

# Assignment 3 — Logic Permissions (and / or)

**What you are doing:**
Deciding if someone can enter based on two pieces of information — their age and whether a parent is with them.
You will use `and` and `or` to combine both conditions into one rule.

---

### Before you start — The rule explained in plain English

```
A person can enter if:
  → they are 13 or older
  OR
  → they are at least 10 AND a parent is with them

Anyone else gets "Sorry, not this time"
```

Let us look at some examples:

| Age | Parent with them? | Can they enter? | Why |
|-----|------------------|----------------|-----|
| 15 | no | YES | Age is 13 or older |
| 11 | yes | YES | Age is at least 10 AND parent is there |
| 11 | no | NO | Not 13+, and no parent |
| 8 | yes | NO | Not 10+, even with a parent |

---

### Step 1 — Create the file

Save a new file as `logic_permissions.py`.

---

### Step 2 — Write the code

```python
# logic_permissions.py
# Decides if someone can enter based on their age and whether a parent is present.

# Ask for age and convert to integer
age = int(input("Enter your age: "))

# Ask if a parent is present — user types y or n
parent = input("Is a parent or guardian with you? (y/n): ")

# Check the rule using and / or with parentheses
if age >= 13 or (age >= 10 and parent == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")
```

---

### Step 3 — What each line does

```
age = int(input(...))        → asks for age, converts text to integer, saves into "age"
parent = input(...)          → asks the y/n question, saves the answer into "parent"

if age >= 13                 → is the person 13 or older? if yes → OK to enter, done
or (age >= 10 and parent == "y")  → OR: are they at least 10 AND is a parent there?
    print("OK to enter")     → one of the conditions above was true
else:
    print("Sorry, not this time")  → none of the conditions were true
```

> **Why use parentheses around `(age >= 10 and parent == "y")`?**
> When you mix `and` and `or` in one line, Python has its own rules about which it checks first
> (similar to how in maths, multiplication happens before addition).
> Parentheses make your rule clear and make sure Python reads it the way you intend.
> Always add parentheses when mixing `and` and `or`.

---

### Step 4 — Run the file

```
python logic_permissions.py
```

**Example run 1 — OK to enter (age 13+):**
```
Enter your age: 15
Is a parent or guardian with you? (y/n): n
OK to enter
```

**Example run 2 — OK to enter (age 10+ with parent):**
```
Enter your age: 11
Is a parent or guardian with you? (y/n): y
OK to enter
```

**Example run 3 — Sorry, not this time:**
```
Enter your age: 9
Is a parent or guardian with you? (y/n): y
Sorry, not this time
```

---

### What to hand in:
`logic_permissions.py` + two example runs — one that prints `"OK to enter"` and one that prints `"Sorry, not this time"`.

---
---

# All Your Files — Copy and Run These

---

### `temperature_input.py`
```python
# Assignment 1
temperature = int(input("Enter a temperature: "))

if temperature >= 25:
    print("warm")
elif temperature >= 15:
    print("ok")
else:
    print("cold")
```

---

### `admin_gate.py`
```python
# Assignment 2
username = input("Enter your username: ")

if username == "admin":
    password = input("Enter your password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

---

### `logic_permissions.py`
```python
# Assignment 3
age = int(input("Enter your age: "))
parent = input("Is a parent or guardian with you? (y/n): ")

if age >= 13 or (age >= 10 and parent == "y"):
    print("OK to enter")
else:
    print("Sorry, not this time")
```

---
---

# Before You Submit — Check This List

Read each line. If you can say YES to all of them, you are ready.

- [ ] Every `if` / `elif` / `else` block is indented correctly (4 spaces or one Tab).
- [ ] I used `==` for comparisons inside `if` — not `=`.
- [ ] When I mixed `and` and `or`, I added parentheses to make the rule clear.
- [ ] All three files run without errors.
- [ ] My example runs match the expected output.

> **Quick reminder on indentation:**
> Every line inside an `if` block must start with 4 spaces (or one Tab).
> If one line is indented differently from the others in the same block, Python will give you an error.

---

