# Name: safia ali
# Program: Simple personal catalog for movies

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
            print("No items in catalog.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
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
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}\n")


def main():
    catalog = Catalog()

    load_catalog("catalog.txt", catalog)

    while True:
        print("\nMy catalog - movies")
        print("1) Add  2) List  3) Save  4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")
            year = int(input("Year: "))

            item = CatalogItem(title, year)

            catalog.add_item(item)

            print("Item added.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog("catalog.txt", catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog("catalog.txt", catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
