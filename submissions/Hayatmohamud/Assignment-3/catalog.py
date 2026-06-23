# Name: Ayoub Jama
# This program manages a simple movie catalog using classes, lists, files, and a menu.

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
            print("No items in the catalog yet.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

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
    file_path = "catalog.txt"
    catalog = Catalog()

    load_catalog(file_path, catalog)

    while True:
        print("\nMy catalog — movies")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

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
            save_catalog(file_path, catalog)
            print("Saved.")

        elif choice == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()