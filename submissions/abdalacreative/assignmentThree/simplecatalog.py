# Abdullaahi Maxamed Axmed
# This program stores movies in a simple catalog system.

from dataclasses import dataclass

# Catalog Item
@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"
# Catalog Class
class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("Catalog is empty.")
        else:
            print("\nMovies in Catalog:")
            for item in self.items:
                print(item)
# Load Catalog From File
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
        # If file does not exist, start with empty catalog
        pass
# Save Catalog To File
def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")

    print("Catalog saved successfully.")

# Main Program
def main():
    file_path = "catalog.txt"

    catalog = Catalog()

    # Load existing data
    load_catalog(file_path, catalog)

    while True:
        print("\n=== Movie Catalog ===")
        print("1) Add Movie")
        print("2) List Movies")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")
        # Add Movie
        if choice == "1":
            title = input("Title: ")

            try:
                year = int(input("Year: "))

                item = CatalogItem(title, year)

                catalog.add_item(item)

                print("Movie added successfully.")

            except ValueError:
                print("Year must be a number.")
        # List Movies
        elif choice == "2":
            catalog.list_all()
        # Save Catalog
        elif choice == "3":
            save_catalog(file_path, catalog)
        # Quit Program
        elif choice == "4":
            save_catalog(file_path, catalog)

            print("Saved. Bye!")

            break
        # Invalid Choice
        else:
            print("Invalid choice. Please select 1-4.")

# Run Program
if __name__ == "__main__":
    main()