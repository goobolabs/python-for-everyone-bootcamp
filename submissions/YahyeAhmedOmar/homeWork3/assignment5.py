# iterate_practice.py

nums = list(range(10))

print(nums[::2])

# Reversed using slicing
print(nums[::-1])

for n in range(3, 8):
    print(n)

words = ["python", "java", "javascript"]

for index, word in enumerate(words):
    print(index, ":", word)

data = {
    "name": "Yahye",
    "course": "Python"
}

for k, v in data.items():
    print(k, "=", v)