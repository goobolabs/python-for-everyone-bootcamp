# Student: Ali-Salad
# Description: A personal movie catalog — add, list, save, and load movies using OOP and file storage.

from dataclasses import dataclass
import random

FILE_PATH = "catalog.txt"


# ── Section 6: @dataclass ──────────────────────────────────────────────────
@dataclass
class CatalogItem:
    title:  str
    year:   int
    genre:  str

    def __str__(self):
        return f"{self.title} ({self.year}) — {self.genre}"


# ── Section 6: Catalog class ───────────────────────────────────────────────
class Catalog:
    def __init__(self):
        self.items: list[CatalogItem] = []

    def add_item(self, item: CatalogItem):
        """Append a CatalogItem to the list."""
        self.items.append(item)

    def list_all(self):
        """Print every item; use __str__ on each CatalogItem."""
        if not self.items:
            print("Catalog is empty. Add a movie first!")
            return
        print("\n── Your Movies ──────────────────────────")
        for i, item in enumerate(self.items, start=1):
            print(f"  {i}. {item}")
        print("─────────────────────────────────────────\n")


# ── Section 4 + 5: load / save ─────────────────────────────────────────────
def load_catalog(path: str, catalog: Catalog):
    """
    Read catalog.txt (title|year|genre per line) into catalog.items.
    If the file is missing, start with an empty list — no crash.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 3:
                    title, year_str, genre = parts
                    # Section 2: validate year is a number before converting
                    if year_str.isdigit():
                        catalog.add_item(CatalogItem(title, int(year_str), genre))
    except FileNotFoundError:
        pass   # first run — start empty, no bare except


def save_catalog(path: str, catalog: Catalog):
    """Write catalog.items back to file, one line per item (title|year|genre)."""
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}|{item.genre}\n")


# ── Section 4: main ────────────────────────────────────────────────────────
def main():
    # Section 1: greeting
    print("══════════════════════════════════")
    print("  🎬  Ali-Salad's Movie Catalog   ")
    print("══════════════════════════════════")

    catalog = Catalog()
    load_catalog(FILE_PATH, catalog)

    if catalog.items:
        print(f"Loaded {len(catalog.items)} saved movie(s).\n")
    else:
        print("No saved movies found. Starting fresh.\n")

    # Section 3 + 2: menu loop with if/elif/else
    while True:
        print("1) Add movie   2) List movies   3) Save   4) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            # --- Add item ---
            title = input("  Title: ").strip()
            if not title:
                print("  Title cannot be empty.\n")
                continue

            # Section 2: validate year with a condition
            year_str = input("  Year:  ").strip()
            if not year_str.isdigit() or not (1888 <= int(year_str) <= 2100):
                print("  Please enter a valid year (e.g. 2026).\n")
                continue

            genre = input("  Genre: ").strip() or "Unknown"
            catalog.add_item(CatalogItem(title, int(year_str), genre))
            print(f"  ✓ Added: {catalog.items[-1]}\n")

        elif choice == "2":
            # --- List items (Section 3: for loop inside list_all) ---
            catalog.list_all()

        elif choice == "3":
            # --- Save ---
            save_catalog(FILE_PATH, catalog)
            print(f"  ✓ Saved {len(catalog.items)} movie(s) to {FILE_PATH}\n")

        elif choice == "4":
            # --- Quit: save then exit loop ---
            save_catalog(FILE_PATH, catalog)
            print(f"Saved. Bye! 👋")
            break

        else:
            print("  Please enter 1, 2, 3, or 4.\n")


# Section 4: guard
if __name__ == "__main__":
    main()