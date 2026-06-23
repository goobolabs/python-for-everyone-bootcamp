# catalog.py
# by: 8o8-nouradin
# Description: A simple personal book catalog for Assignment 3 (Sections 1-6)

from dataclasses import dataclass
@dataclass
class CatalogItem:
    """Represents a single book with a title and release year."""
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"

class Catalog:
    """A class to manage our list of book objects."""
    def __init__(self):
        self.items = []

    def add_item(self, item: CatalogItem):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("The catalog is currently empty.")
        else:
            print("\n--- Current Book List ---")
            # Section 3: Loops
            for book in self.items:
                print(book)
def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    t, y = parts
                    # Create object and add to list
                    catalog.add_item(CatalogItem(t, int(y)))
    except FileNotFoundError:
       pass
def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}\n")
def main():
    filename = "catalog.txt"
    my_catalog = Catalog()
    load_catalog(filename, my_catalog)
    
    print("Welcome to My Personal Book Catalog!")

    while True:
        print("\nMenu: 1) Add  2) List  3) Save  4) Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            year_input = input("Enter release year: ")
            try:
                year = int(year_input)
                new_item = CatalogItem(title, year)
                my_catalog.add_item(new_item)
                print("Book added successfully!")
            except ValueError:
                print("Error: Year must be a number.")

        elif choice == "2":
            my_catalog.list_all()

        elif choice == "3":
            save_catalog(filename, my_catalog)
            print("Catalog saved to file.")

        elif choice == "4":
            save_catalog(filename, my_catalog)
            print("Saved. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

    #output:
    # Welcome to My Personal Book Catalog!
    # Menu: 1) Add  2) List  3) Save  4) Quit
    # Select an option: 1
    # Enter book title: The Great Gatsby
    # Enter release year: 1925
    # Book added successfully!
    # Menu: 1) Add  2) List  3) Save  4) Quit
    # Select an option: 2
    # --- Current Book List ---
    # The Great Gatsby (1925)
    # Menu: 1) Add  2) List  3) Save
    # Select an option: 4
    # Saved. Goodbye!
