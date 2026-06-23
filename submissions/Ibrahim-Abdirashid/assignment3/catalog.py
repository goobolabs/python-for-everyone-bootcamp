# Ibrahim Abdirashid | Personal Movie Catalog - Add, List, Save Movies with OOP

from dataclasses import dataclass
from pathlib import Path


@dataclass
class CatalogItem:
    """Represents a single movie in the catalog."""
    title: str
    year: int

    def __str__(self):
        """Return a readable string representation of the movie."""
        return f"{self.title} ({self.year})"


class Catalog:
    """Manages a collection of catalog items (movies)."""

    def __init__(self):
        """Initialize an empty catalog."""
        self.items = []

    def add_item(self, item):
        """Add a CatalogItem to the catalog."""
        self.items.append(item)

    def list_items(self):
        """Print all items in the catalog in a readable format."""
        if not self.items:
            print("Catalog is empty.")
        else:
            for item in self.items:
                print(f"  • {item}")


def load_catalog(path, catalog):
    """
    Load catalog items from a file.
    File format: title|year (one item per line)
    Raises FileNotFoundError if file doesn't exist.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split("|")
                    if len(parts) == 2:
                        title, year = parts
                        try:
                            item = CatalogItem(title=title, year=int(year))
                            catalog.add_item(item)
                        except ValueError:
                            print(f"Warning: Skipping invalid year '{year}' for '{title}'")
    except FileNotFoundError:
        # File doesn't exist yet; start with empty catalog
        pass


def save_catalog(path, catalog):
    """
    Save catalog items to a file.
    File format: title|year (one item per line)
    """
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    """Main menu loop for the catalog application."""
    catalog_path = "catalog_data.txt"
    catalog = Catalog()

    # Load existing catalog from file
    load_catalog(catalog_path, catalog)

    print("=" * 50)
    print("Welcome to your Personal Movie Catalog!")
    print("=" * 50)

    while True:
        print("\n1) Add   2) List   3) Save   4) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            # Add a new movie
            title = input("Title: ").strip()
            year_input = input("Year: ").strip()
            try:
                year = int(year_input)
                item = CatalogItem(title=title, year=year)
                catalog.add_item(item)
                print(f"✓ Added: {item}")
            except ValueError:
                print("Invalid year. Please enter a number.")

        elif choice == "2":
            # List all movies
            print("\nYour Movies:")
            catalog.list_items()

        elif choice == "3":
            # Save catalog to file
            save_catalog(catalog_path, catalog)
            print(f"✓ Saved {len(catalog.items)} movie(s) to {catalog_path}")

        elif choice == "4":
            # Quit (save first)
            save_catalog(catalog_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
