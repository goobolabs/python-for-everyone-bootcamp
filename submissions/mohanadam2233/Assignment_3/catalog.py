# catalog.py
# Mohamed adam ahmed - Simple personal catalog for books (add, list, save to file).

from dataclasses import dataclass

# ---------- Data model ----------

@dataclass
class CatalogItem:
    title: str
    year: int  # you can change to another field if you like (e.g., author: str)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Catalog:
    def __init__(self):
        self.items = []

    def add(self, item: CatalogItem):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("Catalog is empty.")
        else:
            for item in self.items:
                print(item)


# ---------- File functions ----------

def load_catalog(path: str, catalog: Catalog):
    """Load catalog from a file; if file doesn't exist, start empty."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Expecting format: title|year
                parts = line.split("|")
                if len(parts) != 2:
                    continue  # skip bad lines
                title_str = parts[0]
                year_str = parts[1]
                try:
                    year_int = int(year_str)
                except ValueError:
                    # if year is not an int, skip this line
                    continue
                item = CatalogItem(title=title_str, year=year_int)
                catalog.add(item)
    except FileNotFoundError:
        # Start with empty catalog if file is missing
        pass


def save_catalog(path: str, catalog: Catalog):
    """Save catalog to a file using title|year format."""
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            line = f"{item.title}|{item.year}\n"
            f.write(line)


# ---------- Main program ----------

def main():
    path = "submissions\\mohanadam2233\\Assignment_3\\catalog.txt"
    catalog = Catalog()
    load_catalog(path, catalog)

    print("My catalog — books")

    while True:
        print("1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")
            year_str = input("Year: ")
            try:
                year_int = int(year_str)
            except ValueError:
                print("Year must be a number. Item not added.")
                continue
            item = CatalogItem(title=title, year=year_int)
            catalog.add(item)

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)
            print("Saved.")

        elif choice == "4":
            save_catalog(path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()