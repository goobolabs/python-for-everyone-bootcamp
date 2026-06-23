# Author: [Hibo mohamed]
# catalog.py — A simple movie catalog: add, list, save, and load movies from a file.

from dataclasses import dataclass


# ── Section 6: OOP ───────────────────────

@dataclass
class CatalogItem:
    """Represents a single movie with a title, year, and genre."""
    title: str
    year: int
    genre: str

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) [{self.genre}]"


class Catalog:
    """Holds a collection of CatalogItem objects."""

    def __init__(self) -> None:
        self.items: list[CatalogItem] = []

    def add_item(self, item: CatalogItem) -> None:
        """Add a CatalogItem to the catalog."""
        self.items.append(item)

    def list_all(self) -> None:
        """Print every item; tell the user if the catalog is empty."""
        if not self.items:
            print("  (catalog is empty)")
            return
        # Section 3: loop over the list
        for i, item in enumerate(self.items, start=1):
            print(f"  {i}. {item}")


# ── Section 4: Functions ──────────────────────────────────

DATA_FILE = "catalog.txt"


def load_catalog(path: str, catalog: Catalog) -> None:
    """
    Load items from a UTF-8 text file into catalog.
    Each line has the format:  title|year|genre
    If the file does not exist yet, do nothing (start with an empty catalog).
    Section 5: with open + try/except FileNotFoundError
    """
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 3:
                    continue  # skip malformed lines
                title, year_str, genre = parts
                try:
                    year = int(year_str)
                except ValueError:
                    continue  # skip lines with a bad year
                catalog.add_item(CatalogItem(title=title, year=year, genre=genre))
    except FileNotFoundError:
        pass  # first run — no file yet, start empty


def save_catalog(path: str, catalog: Catalog) -> None:
    """
    Write catalog items back to a UTF-8 text file.
    Each line:  title|year|genre
    Section 5: with open (write mode) + UTF-8 encoding
    """
    with open(path, "w", encoding="utf-8") as fh:
        for item in catalog.items:
            fh.write(f"{item.title}|{item.year}|{item.genre}\n")


def main() -> None:
    """
    Entry point: show a menu, handle user choices.
    Section 1: print / input
    Section 2: if / elif / else on menu choice
    Section 3: list + for loop (inside list_all)
    Section 4: functions called here
    Section 5: load/save with file handling
    Section 6: Catalog + CatalogItem objects
    """
    # Section 1: friendly header
    print("=== My Movie Catalog ===")

    # Section 6 + 5: create catalog object and load from file
    catalog = Catalog()
    load_catalog(DATA_FILE, catalog)

    # Section 3 + 2: main loop with menu
    while True:
        print("\n1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ").strip()

        # Section 2: branching on menu choice
        if choice == "1":
            title = input("  Title: ").strip()
            year_str = input("  Year:  ").strip()
            genre = input("  Genre: ").strip()

            # Simple validation
            try:
                year = int(year_str)
            except ValueError:
                print("  ✗ Year must be a number. Item not added.")
                continue

            if not title:
                print("  ✗ Title cannot be empty. Item not added.")
                continue

            catalog.add_item(CatalogItem(title=title, year=year, genre=genre))
            print(f"  ✓ Added: {catalog.items[-1]}")

        elif choice == "2":
            print("── Catalog ──")
            catalog.list_all()

        elif choice == "3":
            save_catalog(DATA_FILE, catalog)
            print(f"  ✓ Saved {len(catalog.items)} item(s) to '{DATA_FILE}'.")

        elif choice == "4":
            save_catalog(DATA_FILE, catalog)
            print("Saved. Bye!")
            break

        else:
            print("  Please enter 1, 2, 3, or 4.")

# Section 4: guard block
if __name__ == "__main__":
    main()
