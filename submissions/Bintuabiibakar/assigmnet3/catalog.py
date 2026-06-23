
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
    path = "catalog.txt"

    catalog = Catalog()
    load_catalog(path, catalog)

    while True:
        print("\nMy Catalog — Movies")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")

            try:
                year = int(input("Year: "))

                item = CatalogItem(title, year)
                catalog.add_item(item)

                print("Movie added.")

            except ValueError:
                print("Year must be a number.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog(path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()