# Abdullahi

from dataclasses import dataclass


@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if len(self.items) == 0:
            print("Catalog is empty.")
        else:
            print("\nCatalog items:")
            for item in self.items:
                print("-", item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    title = parts[0]
                    year = int(parts[1])

                    item = CatalogItem(title, year)

                    catalog.add_item(item)

    except FileNotFoundError:
        pass


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    catalog = Catalog()

    load_catalog("catalog.txt", catalog)

    while True:
        print("\n1) Add item")
        print("2) List items")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            title = input("Enter title: ")
            year = int(input("Enter year: "))

            item = CatalogItem(title, year)

            catalog.add_item(item)

            print("Item added!")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog("catalog.txt", catalog)

            print("Catalog saved!")

        elif choice == "4":
            save_catalog("catalog.txt", catalog)

            print("Goodbye!")

            break

        else:
            print("Invalid choice. Please choose 1-4.")


if __name__ == "__main__":
    main()




#     PS C:\Users\hp\OneDrive\Desktop\ABDULLAHI\Python> python catalog.py
# Could not find platform independent libraries <prefix>

# 1) Add item
# 2) List items
# 3) Save
# 4) Quit
# Pick: 1
# Enter title: atomic habits
# Enter year: 2008
# Item added!

# 1) Add item
# 2) List items
# 3) Save
# 4) Quit
# Pick: 2

# Catalog items:
# - atomic habits (2008)

# 1) Add item
# 2) List items
# 3) Save
# 4) Quit
# Pick: 4
# Goodbye!