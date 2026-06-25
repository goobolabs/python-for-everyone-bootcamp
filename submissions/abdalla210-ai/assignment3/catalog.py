# Abdullahi Omar Mohamed
# Simple catalog program that loads, saves, and manages catalog items.

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

    def add(self, item: CatalogItem):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("No items in catalog.")
            return
        for item in self.items:
            print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 2:
                    continue
                title, year_str = parts
                try:
                    year = int(year_str)
                except ValueError:
                    continue
                catalog.add(CatalogItem(title, year))
    except FileNotFoundError:
        pass


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    path = "catalog.txt"
    catalog = Catalog()
    load_catalog(path, catalog)

    while True:
        print("\n1: Add")
        print("2: List")
        print("3: Save")
        print("4: Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            year_str = input("Enter year: ")
            try:
                year = int(year_str)
            except ValueError:
                print("Invalid year.")
                continue
            catalog.add(CatalogItem(title, year))

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)
            print("Saved.")

        elif choice == "4":
            save_catalog(path, catalog)
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
