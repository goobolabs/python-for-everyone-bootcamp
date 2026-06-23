# Name: Abdullahi Abdisamed nur
# Program: A simple personal catalog for storing and saving books.

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
        if not self.items:
            print("Catalog is empty.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 2:
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
            title = input("Title: ")
            year_text = input("Year: ")

            if year_text.isdigit():
                year = int(year_text)

                item = CatalogItem(title, year)
                catalog.add_item(item)

                print("Item added.")
            else:
                print("Year must be a number.")

        elif choice == "2":
            print("\nCatalog:")
            catalog.list_all()

        elif choice == "3":
            save_catalog("catalog.txt", catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog("catalog.txt", catalog)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
