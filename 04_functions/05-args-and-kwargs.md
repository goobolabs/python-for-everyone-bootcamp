# `*args` and `**kwargs`

## Theory

Sometimes you want a function to accept **any number** of positional or keyword arguments.

- **`*args`** collects “extra” **positional** arguments into a **tuple** named `args` (the name `args` is convention; the star matters).
- **`**kwargs`** collects “extra” **keyword** arguments into a **dict** named `kwargs`.

You can combine normal parameters, defaults, `*args`, and `**kwargs` with ordering rules (parameters, `*args`, keyword-only, `**kwargs`). For class, use simple patterns first.

## Beginner-friendly notes

- Unpacking at the **call** site uses `*` / `**` too: `f(*list_of_args)`, `f(**dict_of_kwargs)`.
- Use `*args` when “any number of values”; use `**kwargs` for flexible options.

## Example

```python
def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

def profile(name, **info):
    print("Name:", name)
    for key, value in info.items():
        print(" ", key, ":", value)

print(total(1, 2, 3))
print(total())
profile("Lee", city="Oslo", role="dev")
```

## Expected output

```text
6
0
Name: Lee
  city : Oslo
  role : dev
```

(Exact spacing may vary slightly; keys in dict iteration order follow insertion.)

## Mini practice

1. Write `def first_and_rest(head, *tail):` that prints `head` and the length of `tail`. Call with several numbers.
2. Write `def merge_defaults(**opts):` that returns a dict starting with `{"theme": "light"}` updated with anything passed in `opts` (hint: copy then update, or build a new dict).

Continue with `06-scope.md`.
