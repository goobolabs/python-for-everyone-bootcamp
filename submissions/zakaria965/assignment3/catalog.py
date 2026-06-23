# Zakaria - Personal movie catalog program

from dataclasses import dataclass

@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        for item in self.items:
            print(item)

def load_catalog(path, catalog):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    title, year_str = parts
                    try:
                        year = int(year_str)
                        item = CatalogItem(title, year)
                        catalog.add_item(item)
                    except ValueError:
                        pass  # skip invalid lines
    except FileNotFoundError:
        pass  # start empty if file not found

def save_catalog(path, catalog):
    with open(path, 'w', encoding='utf-8') as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}\n")

def main():
    catalog = Catalog()
    load_catalog('catalog.txt', catalog)
    while True:
        print("My catalog — movies")
        print("1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ").strip()
        if choice == '1':
            title = input("Title: ").strip()
            year_str = input("Year: ").strip()
            try:
                year = int(year_str)
                item = CatalogItem(title, year)
                catalog.add_item(item)
            except ValueError:
                print("Invalid year")
        elif choice == '2':
            catalog.list_items()
        elif choice == '3':
            save_catalog('catalog.txt', catalog)
            print("Saved.")
        elif choice == '4':
            save_catalog('catalog.txt', catalog)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()