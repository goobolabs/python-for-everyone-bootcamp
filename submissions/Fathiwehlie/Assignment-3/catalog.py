# Fathi Abdirahman Mohamed
# Simple personal catalog program for storing and managing movies.
# Fathi Wehlie
# Simple personal catalog program for storing and managing movies.

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
            return

        print("\nMovies in catalog:")
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

    print("Catalog saved.")


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

            year_input = input("Year: ")

            try:
                year = int(year_input)

                item = CatalogItem(title, year)
                catalog.add_item(item)

                print("Movie added.")

            except ValueError:
                print("Year must be a number.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(file_path, catalog)

        elif choice == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()