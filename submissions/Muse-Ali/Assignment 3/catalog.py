# Author: muse Alinor 
# A personal movie catalog: add, list, save, and load movies from a file.

from dataclasses import dataclass   # Section 6 – OOP / dataclass
import sys                          # Section 5 – used for clean exit messaging


# ── Section 6: OOP ────────────────────────────────────────────────────────────

@dataclass
class CatalogItem:
    """One movie entry with a title, year, and genre."""
    title: str
    year: int
    genre: str

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) [{self.genre}]"


class Catalog:
    """Holds a collection of CatalogItem objects and exposes add / list_all."""

    def __init__(self) -> None:
        self.items: list[CatalogItem] = []   # Section 3 – list

    def add_item(self, item: CatalogItem) -> None:
        self.items.append(item)

    def list_all(self) -> None:
        if not self.items:
            print("  (no movies yet)")
            return
        for i, item in enumerate(self.items, start=1):   # Section 3 – for loop
            print(f"  {i}. {item}")                       # Section 6 – __str__


# ── Section 4: Functions ──────────────────────────────────────────────────────

DATA_FILE = "catalog.txt"


def load_catalog(path: str, catalog: Catalog) -> None:
    """Read title|year|genre lines into catalog.items."""
    try:                                                  # Section 5 – try/except
        with open(path, encoding="utf-8") as fh:         # Section 5 – with open
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 3:
                    continue                             # skip malformed lines
                title, year_str, genre = parts
                try:
                    year = int(year_str)
                except ValueError:
                    continue                             # skip bad year
                catalog.add_item(CatalogItem(title=title, year=year, genre=genre))
    except FileNotFoundError:                            # Section 5 – specific exception
        pass                                             # first run → start empty


def save_catalog(path: str, catalog: Catalog) -> None:
    """Write catalog.items back to file in title|year|genre format."""
    with open(path, "w", encoding="utf-8") as fh:       # Section 5 – with open
        for item in catalog.items:                       # Section 3 – for loop
            fh.write(f"{item.title}|{item.year}|{item.genre}\n")


def main() -> None:
    """Entry point: build catalog, load data, run menu loop."""
    # Section 1 – print / intro
    print("=" * 40)
    print("   🎬  My Movie Catalog")
    print("=" * 40)

    catalog = Catalog()                  # Section 6 – instantiate class
    load_catalog(DATA_FILE, catalog)     # Section 4 – call function

    # Section 3 – while loop;  Section 2 – conditions on menu choice
    while True:
        print("\n1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ").strip()   # Section 1 – input

        if choice == "1":                  # Section 2 – if / elif / else
            title = input("Title: ").strip()
            if not title:
                print("  Title cannot be empty.")
                continue

            year_str = input("Year:  ").strip()
            try:
                year = int(year_str)
            except ValueError:
                print("  Year must be a whole number.")
                continue

            genre = input("Genre: ").strip()
            if not genre:
                genre = "Unknown"

            catalog.add_item(CatalogItem(title=title, year=year, genre=genre))
            print(f'  Added "{title}".')

        elif choice == "2":
            print()
            catalog.list_all()

        elif choice == "3":
            save_catalog(DATA_FILE, catalog)   # Section 4 – call function
            print("  Saved.")

        elif choice == "4":
            save_catalog(DATA_FILE, catalog)   # save on quit
            print("Saved. Bye!")
            break

        else:
            print("  Please enter 1, 2, 3, or 4.")


# ── Section 4: guard ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
