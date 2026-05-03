# loop_control.py

# Stop loop when number becomes greater than 6
for n in range(15):
    if n > 6:
        break
    print(n)

print("----")

for n in range(10):
    if n == 4:
        continue
    print(n)

if False:
    pass