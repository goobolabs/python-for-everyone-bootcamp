# flexible_report.py

def total(*numbers):
    return sum(numbers)

def profile(**info):
    for key, value in info.items():
        print(key, ":", value)

print(total(1, 2, 3))
print(total(10, 20))
print(total())

print("-----")

profile(name="Yahye", age=20, course="Python")

print("-----")

profile(name="Ahmed", city="Mogadishu")