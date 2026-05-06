# `try`, `except`, `finally`

## Theory

**Exceptions** signal errors or unusual conditions. You can **catch** them so the program does not crash.

```python
try:
    risky_code()
except ValueError as e:
    print("bad value:", e)
finally:
    cleanup_always_runs()
```

- **`try`:** run this first.
- **`except SomeError`:** run if that error (or subclass) was raised. You can have multiple `except` clauses.
- **`else`:** optional; runs if **no** exception in `try`.
- **`finally`:** optional; runs **always** after `try`/`except`/`else` (even if `return` or exception).

Catch **specific** exceptions (`ValueError`, `FileNotFoundError`) instead of a bare `except:` that hides bugs.

## Beginner-friendly notes

- Read tracebacks bottom-up: last line is the **error type and message**; lines above show the call stack.
- `raise` re-raises the current exception inside an `except` block if you partially handle it.

## Example

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("cannot divide by zero")
        return None
    finally:
        print("done with divide")

print(divide(10, 2))
print(divide(10, 0))
```

## Expected output

```text
done with divide
5.0
cannot divide by zero
done with divide
None
```

## Mini practice

1. Wrap `int(input())` in `try`/`except ValueError` and prompt again until the user enters an integer (reuse Section 2 ideas).
2. Open a **nonexistent** file in `try`, catch `FileNotFoundError`, print a friendly message.
3. Add `finally` that prints `"cleanup"` and verify it runs on success and failure.

---

**End of Section 5 (File handling and error handling).** Complete `homework.md`, then continue to **`06_object_oriented_programming`** (`01-classes-and-objects.md`).
