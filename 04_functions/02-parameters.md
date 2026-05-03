# Parameters

## Theory

**Parameters** are names listed in the **`def`** header—they stand for values the caller will supply. **Arguments** are the **actual values** passed at **call** time.

Kinds you will use early:

- **Positional:** `def f(a, b):` — `f(1, 2)` binds `a=1`, `b=2` by **position**.
- **Keyword:** `f(b=2, a=1)` — names match parameters; order can differ.

**Keyword-only** parameters (after `*`) and other advanced forms exist; focus on positional + keyword first.

## Beginner-friendly notes

- “Parameter” = in the **definition**; “argument” = in the **call** (many people use them loosely—precision helps when debugging).
- Match **arity**: `f` expects two args—pass two (unless defaults exist—next lesson).

## Example

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))
print(power(exponent=3, base=2))
```

## Expected output

```text
8
8
```

## Mini practice

1. Write `def introduce(first, last):` that prints `first` and `last` on one line. Call it **positionally** and again with **keywords**.
2. What happens if you call `introduce(last="Lovelace", first="Ada")`? Predict, then run.

Continue with `03-return-values.md`.
