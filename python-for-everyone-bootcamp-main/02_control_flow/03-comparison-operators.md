# Comparison operators

## Theory

**Comparison operators** compare two values and produce **`True`** or **`False`**.

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal |
| `>=` | greater than or equal |

These work as expected for numbers. For strings, comparisons use **lexicographic** (dictionary-like) order, which can surprise beginners—`'10' < '2'` is `True` because character-by-character rules differ from numeric order.

**Chaining:** Python allows math-like chains: `0 <= x <= 10` means `x` is between 0 and 10 inclusive.

## Beginner-friendly notes

- Always use **`==`** in conditions, not `=` (assignment).
- Compare **compatible** types when possible; mixed types may work in Python 3 in limited cases but often you should convert explicitly (e.g. compare numbers to numbers).
- Floating point: `0.1 + 0.2 == 0.3` can be `False` due to binary floating point. For money or exact decimals, later you might use `decimal.Decimal`; for class, compare with tolerance or round first.

## Example

```python
a = 7
b = 10

print(a == b)
print(a != b)
print(a < b)
print(5 <= a <= 9)
```

## Expected output

```text
False
True
True
True
```

## Mini practice

1. Set `score = 88`. Print whether `score` is **greater than or equal to** `80` (print the `True` or `False` result).
2. Set `name = "Ada"`. Print whether `name` is **equal to** `"Ada"` using `==`.

Continue with `04-logical-operators.md`.
