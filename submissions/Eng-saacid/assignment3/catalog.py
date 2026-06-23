
# Eng Saacid Abdi Aziiz
# This program manages a small catalog of books, movies, or games.

from dataclasses import dataclass


@dataclass
class CatalogItem:
    title: str
    category: str
    year: int


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, title, category, year):
        item = CatalogItem(title, category, year)
        self.items.append(item)

    def list_items(self):
        if not self.items:
            print("No items in the catalog.")
            return

        for item in self.items:
            print(f"{item.title}, {item.category}, ({item.year})")

    def save_to_file(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for item in self.items:
                file.write(f"{item.title},{item.category},{item.year}\n")

    def load_from_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    title, category, year = line.strip().split(",")
                    self.add_item(title, category, int(year))

        except FileNotFoundError:
            print("File not found. Starting with an empty catalog.")


def main():
    catalog = Catalog()
    catalog.load_from_file("catalogs.txt")

    while True:
        print("\nMy Catalog books:")
        print("1 = Add item")
        print("2 = List items")
        print("3 = Save")
        print("4 = Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ").strip()
            category = input("Enter category: ").strip()

            while True:
                try:
                    year = int(input("Enter year: ").strip())
                    break
                except ValueError:
                    print("Year must be a number. Try again.")

            catalog.add_item(title, category, year)
            print("Item added.")

        elif choice == "2":
            print("\nCatalog items:")
            catalog.list_items()

        elif choice == "3":
            catalog.save_to_file("catalogs.txt")
            print("Catalog saved.")

        elif choice == "4":
            catalog.save_to_file("catalogs.txt")
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

    