# calculator_calls.py

# Parameters are variables in the function definition.
# Arguments are the actual values passed to the function.

def multiply(a, b):
    return a * b

result1 = multiply(3, 4)
result2 = multiply(b=5, a=2)

print("Positional arguments result:", result1)
print("Keyword arguments result:", result2)