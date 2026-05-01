# Nested conditions

## Theory

A **nested condition** is an `if` (or `if`/`elif`/`else`) **inside** another branch. Use this when a decision depends on **more than one** fact, and the second check only matters if the first is true (or false).

Example pattern:

```text
if outer_condition:
    if inner_condition:
        ...
    else:
        ...
else:
    ...
```

Often you can **flatten** logic with `and` / `or` (next lessons). Nested `if`s are fine when they match how you think about the problem—but avoid **very deep** nesting (many levels); it becomes hard to read.

## Beginner-friendly notes

- Ask: “Can I say this as one condition?” If yes, combining with `and`/`or` may be clearer.
- Each level must be indented consistently (usually +4 spaces per level).
- `else` pairs with the **nearest** `if` at the same indentation level.

## Example

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the show.")
    else:
        print("You need a ticket.")
else:
    print("Sorry, minors not allowed.")
```

## Expected output

```text
Welcome to the show.
```

Try `has_ticket = False` and `age = 16` in separate runs to see the other messages.

## Mini practice

1. Ask for a **username** with `input()`. If it is `"admin"`, ask for a **password**; if the password is `"secret"`, print `"Access granted"`, else print `"Wrong password"`. If the username is not `admin`, print `"Unknown user"` (do not ask for a password).

When you are ready, open `homework.md` in this folder and complete the section assignments.
