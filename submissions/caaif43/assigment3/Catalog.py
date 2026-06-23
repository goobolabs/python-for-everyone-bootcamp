
# Caaif
# Simple movie catalog program

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
            print("No movies in catalog.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    title, year = line.split("|")

                    item = CatalogItem(
                        title,
                        int(year)
                    )

                    catalog.add_item(item)

    except FileNotFoundError:
        print("No catalog file found. Starting empty.")


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")

    print("Catalog saved.")


def main():
    catalog = Catalog()

    load_catalog("catalog.txt", catalog)

    while True:
        print("\n--- Movie Catalog ---")
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Save")
        print("4. Quit")

        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")
            year = int(input("Year: "))

            item = CatalogItem(title, year)

            catalog.add_item(item)

            print("Movie added.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog("catalog.txt", catalog)

        elif choice == "4":
            save_catalog("catalog.txt", catalog)

            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
