# Dictionaries

## Theory

A **dictionary** (`dict`) maps **keys** to **values**. Keys must be **unique** and **hashable** (strings, numbers, tuples of immutables, etc.). Values can be any type.

- **Literal:** `{"name": "Ada", "year": 1815}` or `{}` for empty.
- **Access:** `d["name"]` raises **KeyError** if key is missing. (Dicts use **keys**, not numeric positions; for **list-style** indexing and **slicing** of sequences, use the **Lists** lesson.)
- **Safe access:** `d.get("name", default)` returns `default` if key is absent.
- **Add / update:** `d["key"] = value`
- **Delete:** `del d["key"]` or `d.pop("key")`

**Order:** In Python 3.7+, dicts **preserve insertion order** (implementation detail that became language feature).

## Beginner-friendly notes

- Think “real dictionary”: look up a **word** (key), get a **definition** (value).
- Use `.get()` when the key might not exist (user input, optional fields).
- Keys are often strings; values might be lists, numbers, or nested dicts.
- **Looping** over a dict with `for` comes in the next lesson (`05-for-loops.md`); here we only **look up** and **print** what we need without a loop.

## Example

```python
student = {"name": "Maya", "grade": 92}
print(student["name"])
print(student.get("email", "no email"))

student["email"] = "maya@example.com"
print(student.get("email"))

# See all keys and values (no loop yet—next lesson)
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("as a whole:", student)
```

## Expected output

```text
Maya
no email
maya@example.com
keys: ['name', 'grade', 'email']
values: ['Maya', 92, 'maya@example.com']
as a whole: {'name': 'Maya', 'grade': 92, 'email': 'maya@example.com'}
```

## Mini practice

1. Build a dict with three **country → capital** pairs. Print **all keys** and **all values** using `.keys()` and `.values()` (wrap with `list(...)` if you want a readable list).
2. Use `.get()` to look up a country not in your dict with default `"unknown"`.
3. Update one capital and print the dict before and after.

Continue with `05-for-loops.md`.
