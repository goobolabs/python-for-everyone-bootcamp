# name Abdihamid Hussein
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
            print("Catalog is empty.")
            return

        for item in self.items:
            print(item)

def load_catalog(path, catalog: Catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) != 2:
                    continue

                title = parts[0]
                try:
                    year = int(parts[1])
                except ValueError:
                    continue

                catalog.add(CatalogItem(title, year))

    except FileNotFoundError:
        
        pass


def save_catalog(path, catalog: Catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")

def main():
    FILE_NAME = "catalog.txt"

    catalog = Catalog()
    load_catalog(FILE_NAME, catalog)

    while True:
        print("\n--- CATALOG MENU ---")
        print("1. Add item")
        print("2. List items")
        print("3. Save")
        print("4. Quit")

        choice = input("Choose option: ")
        if choice == "1":
            title = input("Enter title: ").strip()

            try:
                year = int(input("Enter year: "))
            except ValueError:
                print("Year must be a number.")
                continue

            catalog.add(CatalogItem(title, year))
            print("Item added.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(FILE_NAME, catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog(FILE_NAME, catalog)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

main()