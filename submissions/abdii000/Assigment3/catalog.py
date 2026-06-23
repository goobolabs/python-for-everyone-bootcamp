# Name: Abdirahman Hassan
# Program: A simple catalog system to store and manage movies using OOP and file handling

from dataclasses import dataclass

# Section 6: Object-Oriented Programming
@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"


class Catalog:
    def __init__(self):
        self.items = []  # Section 3: List

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("Catalog is empty.")
        else:
            for item in self.items:
                print(item)


# Section 5: File Handling + Error Handling
def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    title, year = line.split("|")
                    catalog.items.append(CatalogItem(title, int(year)))
    except FileNotFoundError:
        # First run: file doesn't exist → start empty
        pass


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
        print("\nMy Movie Catalog")
        print("1) Add  2) List  3) Save  4) Quit")

        choice = input("Pick: ")

        # Section 2: Conditions
        if choice == "1":
            title = input("Title: ")
            year_input = input("Year: ")

            if year_input.isdigit():
                year = int(year_input)
                item = CatalogItem(title, year)
                catalog.add_item(item)
                print("Item added.")
            else:
                print("Invalid year. Please enter a number.")

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
            print("Invalid choice. Try again.")


# Section 4: Entry point
if __name__ == "__main__":
    main()