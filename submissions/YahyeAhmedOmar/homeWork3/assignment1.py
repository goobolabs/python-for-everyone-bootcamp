# list_toolkit.py

cities = ["Mogadishu", "Hargeisa", "Kismayo", "Bosaso", "Baidoa"]

print("First item:", cities[0])
print("Last item:", cities[-1])

cities.append("Garowe")
print("Updated list:", cities)

# Removed item using remove()
cities.remove("Kismayo")

print("After removal:", cities)
print("Length of list:", len(cities))