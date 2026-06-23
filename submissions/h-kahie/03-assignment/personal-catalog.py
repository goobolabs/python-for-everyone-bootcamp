# Name: H-Kahie
# Program: Simple personal catalog for storing books using OOP, files, functions, and loops

from dataclasses import dataclass

@dataclass
class CatalogItem:
    title: str
    year: int

    
    def __str__(self):
        return f"{self.title} ({self.year})"


class Catalog:

    def __init__(self):
        # Empty list to store all items
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):

        if len(self.items) == 0:
            print("Catalog is empty.")
            return

        print("\n--- My Catalog ---")

        for item in self.items:
            print(item)


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
        pass


def save_catalog(path, catalog):

    with open(path, "w", encoding="utf-8") as file:

        for item in catalog.items:

            # Save in this format:
            # title|year
            file.write(f"{item.title}|{item.year}\n")

    print("Catalog saved successfully.")


# Main program
def main():

    # File name
    path = "catalog.txt"

    # Create catalog object
    catalog = Catalog()

    load_catalog(path, catalog)

    while True:

        print("\n===== PERSONAL CATALOG =====")
        print("1) Add Item")
        print("2) List Items")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        # Add item
        if choice == "1":

            title = input("Title: ")

            try:
                year = int(input("Year: "))

                item = CatalogItem(title, year)

                catalog.add_item(item)

                print("Item added successfully.")

            except ValueError:
                print("Please enter a valid number for year.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)

        elif choice == "4":

            save_catalog(path, catalog)

            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
