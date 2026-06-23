# Name: Abdiaziz Bishar Hussein
# Description: A terminal-based personal movie catalog manager using OOP, file handling, and collections.

from dataclasses import dataclass

@dataclass
class CatalogItem:
    """Represents a single item in the catalog."""
    title: str
    year: int

    def __str__(self) -> str:
        """Optional: Custom string representation for nicer printing."""
        return f"{self.title} ({self.year})"


class Catalog:
    """Manages a collection of CatalogItem objects."""
    def __init__(self):
        self.items: list[CatalogItem] = []

    def add_item(self, item: CatalogItem) -> None:
        """Adds a CatalogItem to the internal list."""
        self.items.append(item)

    def list_all(self) -> None:
        """Prints all items in a readable format."""
        if not self.items:
            print("\nYour catalog is currently empty.")
            return
        
        print("\n--- Current Catalog Items ---")
        for index, item in enumerate(self.items, 1):
            print(f"{index}. {item}")
        print("----------------------------")


def load_catalog(path: str, catalog: Catalog) -> None:
    """Loads catalog data from a text file. Handles FileNotFoundError gracefully."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Strip newline characters and skip empty lines
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                # Split line by the pipe character
                title, year_str = cleaned_line.split("|")
                
                # Create the item and add it to the catalog
                item = CatalogItem(title=title, year=int(year_str))
                catalog.add_item(item)
        print(f"\n[System] Successfully loaded data from {path}.")
    except FileNotFoundError:
        # If missing, do nothing and start with an empty catalog as required
        print(f"\n[System] '{path}' not found. Starting with a fresh catalog.")
    except (ValueError, IndexError):
        print(f"\n[Warning] Found corrupted data line in '{path}'. Skipping bad entry.")


def save_catalog(path: str, catalog: Catalog) -> None:
    """Saves the catalog items back to the text file using the 'title|year' format."""
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")
    print(f"[System] Catalog successfully saved to '{path}'.")


def main():
    # Initialize the catalog tracking object
    catalog = Catalog()
    data_file = "catalog_data.txt"
    
    # Load any existing data before entering the interactive loop
    load_catalog(data_file, catalog)
    
    while True:
        print("\nMy Catalog — Movies")
        print("1) Add  2) List  3) Save  4) Quit")
        
        choice = input("Pick (1-4): ").strip()
        
        if choice == "1":
            title = input("Title: ").strip()
            if not title:
                print("Title cannot be empty. Item not added.")
                continue
                
            try:
                year = int(input("Year: ").strip())
                new_item = CatalogItem(title=title, year=year)
                catalog.add_item(new_item)
                print(f"Added: {new_item}")
            except ValueError:
                print("Invalid input. Year must be a valid integer. Item not added.")
                
        elif choice == "2":
            catalog.list_all()
            
        elif choice == "3":
            save_catalog(data_file, catalog)
            
        elif choice == "4":
            print("\nSaving final changes...")
            save_catalog(data_file, catalog)
            print("Saved. Bye!")
            break
            
        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()