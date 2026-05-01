# Assignment operators

## Theory

You already know **`=`** assigns a value to a name. Python also has **compound assignment operators** that update a variable in place using the current value:

| Operator | Same as |
|----------|---------|
| `x += n` | `x = x + n` |
| `x -= n` | `x = x - n` |
| `x *= n` | `x = x * n` |
| `x /= n` | `x = x / n` |
| `x //= n` | `x = x // n` |
| `x %= n` | `x = x % n` |
| `x **= n` | `x = x ** n` |

These are **shorthand** for readability when you modify one variable repeatedly.

**Walrus operator** (`:=`) exists in Python 3.8+ but is optional for beginners; this course does not require it yet.

## Beginner-friendly notes

- The name on the left must already exist (or you are creating it with `=`). For `+=`, `x` must refer to something that supports the operation (numbers, some sequences).
- Style: use `+=` when it makes the intent “accumulate” or “adjust” clearer than repeating the variable name.

## Example

```python
score = 10
print("start:", score)

score += 5   # same as score = score + 5
print("after += 5:", score)

score *= 2
print("after *= 2:", score)

score -= 3
print("after -= 3:", score)

# Remainder example
n = 10
n %= 3
print("10 % 3 as remainder:", n)
```

## Expected output

```text
start: 10
after += 5: 15
after *= 2: 30
after -= 3: 27
10 % 3 as remainder: 1
```

## Mini practice

1. Set `balance = 100`. Subtract `25` using `-=`. Add `10` using `+=`. Print `balance` (you should see `85`).
2. Set `word = "Hi"`. Use `+=` to append `" there"`. Print `word`.

Continue with `03-comparison-operators.md`.
