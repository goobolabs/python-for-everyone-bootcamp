# by MUHIYADIN2025
# Description: A simple catalog program to add, list, save, and load items (movies/books/games)

from dataclasses import dataclass

# Section 6: OOP
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


# Section 5: File handling
def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    title, year = line.split("|")
                    catalog.items.append(CatalogItem(title, int(year)))
    except FileNotFoundError:
        pass  # haddii file uusan jirin, catalog empty ayuu bilaabanayaa


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


# Section 4: Functions + main
def main():
    catalog = Catalog()
    file_path = "catalog.txt"

    load_catalog(file_path, catalog)

    while True:
        print("\nMy Catalog")
        print("1) Add  2) List  3) Save  4) Quit")

        choice = input("Pick: ")

        # Section 2: Conditions
        if choice == "1":
            title = input("Title: ")
            try:
                year = int(input("Year: "))
                item = CatalogItem(title, year)
                catalog.add_item(item)
            except ValueError:
                print("Year must be a number.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(file_path, catalog)
            print("Saved!")

        elif choice == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Try again.")


# Section 4: Entry point
if __name__ == "__main__":
    main()