# Common methods

## Theory

Python objects expose **methods** (functions attached to the object) you call with **dot** syntax: `obj.method(...)`.

Below are **common** methods—**not** every method on every type. Use `help(list)` or official docs when you need the full list.

### Lists (`list`)

| Method | Effect |
|--------|--------|
| `.append(x)` | add `x` at end |
| `.extend(iterable)` | append all items from iterable |
| `.insert(i, x)` | insert `x` at index `i` |
| `.remove(x)` | remove first occurrence of `x` (ValueError if missing) |
| `.pop(i=-1)` | remove and return item at index |
| `.sort()` | sort in place; `sort(reverse=True)` |
| `.reverse()` | reverse in place |

### Strings (`str`)

| Method | Effect |
|--------|--------|
| `.strip()` | remove leading/trailing whitespace |
| `.lower()` / `.upper()` | case change (new string) |
| `.split(sep)` | split into list by separator |
| `.replace(a, b)` | replace substring |

### Dicts (`dict`)

| Method | Effect |
|--------|--------|
| `.get(k, default)` | safe lookup |
| `.keys()`, `.values()`, `.items()` | views of contents |
| `.pop(k)` | remove and return value |

### Sets (`set`)

| Method | Effect |
|--------|--------|
| `.add(x)` | add element |
| `.discard(x)` | remove if present |

## Beginner-friendly notes

- Methods that say **in place** modify the object; many string methods **return new strings** because strings are immutable.
- **`sorted(list)`** is a **function** that returns a new sorted list; **`.sort()`** sorts the list itself and returns `None`.

## Example

```python
nums = [3, 1, 2]
nums.sort()
print(nums)

text = "  Hello  "
print(text.strip().lower())

d = {"a": 1}
print(d.get("b", 0))

bag = {1, 2}
bag.add(3)
print(bag)
```

## Expected output

```text
[1, 2, 3]
hello
0
{1, 2, 3}
```

## Mini practice

1. Start with `[4, 1, 3]`, sort **descending** with `.sort(reverse=True)`, print.
2. Take `"a,b,c"`, use `.split(",")` and print the resulting list.
3. Create a dict, use `.pop("missing", None)` pattern—actually `pop` takes default as second arg in Python: `d.pop("missing", None)`—look up behavior and try with a key that exists and one that does not.

---

**End of Section 3 (Collections, loops, and methods).** Complete `homework.md`, then continue to **Section 4: Functions and Modules** when it is available.
