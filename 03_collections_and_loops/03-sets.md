# Sets

## Theory

A **set** is an **unordered** collection of **unique** items. Duplicate values are collapsed; membership tests are typically **fast**.

- **Literal:** curly braces `{1, 2, 3}` or `set()` for empty (**not** `{}`—that creates an empty **dict**).
- **From iterable:** `set([1, 2, 2])` → `{1, 2}`.
- **Add / remove:** `.add(x)`, `.remove(x)` (error if missing), `.discard(x)` (no error if missing).

**Limitation:** items must be **hashable** (immutable types like numbers, strings, tuples of immutables). Lists cannot be set elements.

**Operations:** union `|`, intersection `&`, difference `-`, symmetric difference `^`.

## Beginner-friendly notes

- If you need **order** or **duplicates**, use a list, not a set.
- Use sets to **deduplicate** or to test “is this value one of many allowed values?” quickly.
- Printing a set may show elements in any order—do not rely on order.

## Example

```python
tags = {"python", "code", "python", "learn"}
print(tags)

tags.add("fun")
print("code" in tags)

a = {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)
print("intersection:", a & b)
```

## Expected output

(Exact order of set contents may vary.)

```text
{'learn', 'python', 'code'}
True
union: {1, 2, 3, 4, 5}
intersection: {3}
```

## Mini practice

1. Start with `letters = ["a", "b", "a", "c", "b"]`. Build `set(letters)` and print it.
2. Create two sets of numbers and print their **intersection** and **difference**.
3. Try `{{1, 2}}` in your head—why is a set of sets not written that way? (Hint: sets are not hashable.) Optional: read about `frozenset` later.

Continue with `04-dictionaries.md`.
