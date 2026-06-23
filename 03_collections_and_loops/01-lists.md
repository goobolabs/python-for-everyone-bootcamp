# Lists

## Theory

A **list** is an **ordered** collection of items. Items can be any type (even mixed), and lists are **mutable**: you can change them after creation.

- **Literal:** square brackets `[1, 2, 3]` or `[]` for empty.
- **Order matters:** same items in different order are different lists.
- **Duplicates allowed:** `[1, 1, 1]` is valid.

Common operations you will use often:

- **Index:** `items[0]` is first, `items[-1]` is last.
- **Slice:** `items[1:3]` — sub-ranges; see **Indexing and slicing** below.
- **Length:** `len(items)`.
- **Add to end:** `items.append(x)`.
- **Insert:** `items.insert(i, x)`.
- **Remove:** `items.remove(value)`, `items.pop(index)`.

## Beginner-friendly notes

- Think of a list as a **row of labeled slots** numbered `0`, `1`, `2`, …
- `append` is **in place**—it modifies the list; it does not create a new list.
- Out-of-range indices raise `IndexError`.
- Slicing **out of range** is safe (it clips); indexing one past the end raises `IndexError`.

## Indexing and slicing

**Indexing** picks one element by position. **Slicing** picks a **sub-range** of elements. The same rules apply to **strings** and **tuples** later.

- **Indices start at 0.** Last item: `s[-1]`, second-to-last: `s[-2]`.
- **Slice:** `s[start:stop]` — from `start` up to **but not including** `stop`.
- **Omitted bounds:** `s[:3]` first three items; `s[2:]` from index 2 to end; `s[:]` shallow copy of the list.
- **Step:** `s[start:stop:step]` — e.g. every second item: `s[::2]`; **reverse:** `s[::-1]`.

**Off-by-one:** `range(3)` is `0,1,2`; slice `0:3` covers indices `0,1,2`.

## Example

```python
scores = [88, 92, 79]
print(scores[0])
print(scores[1:3])  # 79 is index 2 — slice end is exclusive
scores.append(95)
print(scores)
print("count:", len(scores))

empty = []
empty.append("first")
print(empty)

nums = [10, 20, 30, 40, 50]
print(nums[::2])   # every other
print(nums[::-1])  # reversed
```

## Expected output

```text
88
[92, 79]
[88, 92, 79, 95]
count: 4
['first']
[10, 30, 50]
[50, 40, 30, 20, 10]
```

## Mini practice

1. Create `names = ["Ada", "Lin", "Alan"]`. Replace the middle name with another string. Print `names`.
2. Remove `"Alan"` with `.remove("Alan")` or `.pop()`. Print the list.
3. Create two lists and **concatenate** them with `+` into a new list. Print it.
4. For `words = ["one", "two", "three", "four"]`, print a slice with **only** `"two"` and `"three"` (use a `start:stop` slice).

Continue with `02-tuples.md`.
