# Yusra Mohamed
# Movie catalog program

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
        if len(self.items) == 0:
            print("Catalog is empty.")
        else:
            print("\nMovies in Catalog:")
            for item in self.items:
                print(item)


# File Handling
def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split("|")

                
                if len(parts) == 2:
                    title = parts[0]
                    year = int(parts[1])

                    item = CatalogItem(title, year)
                    catalog.add_item(item)

    except FileNotFoundError:
        print("No catalog file found. Starting empty")


# Save
def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    catalog = Catalog()
    file_name = "catalog.txt"

    load_catalog(file_name, catalog)

    while True:
        print("\nMy Movie Catalog")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            title = input("Enter movie title: ")

            
            try:
                year = int(input("Enter movie year: "))
            except ValueError:
                print("Invalid year. Please enter a number")
                continue

            item = CatalogItem(title, year)
            catalog.add_item(item)

            print("Movie added")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(file_name, catalog)
            print("Catalog saved successfully.")

        elif choice == "4":
            save_catalog(file_name, catalog)
            print("Saved Goodbye!")
            break

        else:
            print("Invalid choice try again")


if __name__ == "__main__":
    main()