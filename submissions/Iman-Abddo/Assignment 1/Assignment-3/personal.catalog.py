# Abdulqadir
# Simple catalog program for storing and listing items

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

    def add(self, item):
        self.items.append(item)

    def list_all(self):

        if not self.items:
            print("Catalog is empty.")

        else:
            print("\nCatalog Items:")

            for item in self.items:
                print(item)


def load_catalog(path, catalog):

    try:
        with open(path, "r", encoding="utf-8") as f:

            for line in f:

                title, year = line.rstrip("\n").split("|")

                item = CatalogItem(title, int(year))

                catalog.add(item)

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

        print("\nMy Catalog — Movies")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":

            title = input("Title: ")
            year = int(input("Year: "))

            item = CatalogItem(title, year)

            catalog.add(item)

            print("Movie added!")

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
            print("Invalid choice")


if __name__ == "__main__":
    main()
