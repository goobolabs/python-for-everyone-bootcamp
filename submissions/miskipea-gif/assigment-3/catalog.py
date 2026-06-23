# Student catalog — a simple movie catalog with add, list, save, and quit options.

from dataclasses import dataclass
import os

DATA_FILE = "catalog_data.txt"


@dataclass
class CatalogItem:
    title: str
    year: int
    kind: str  

    def __str__(self):
        return f"{self.title} ({self.year}) [{self.kind}]"


class Catalog:
    def __init__(self):
        self.items: list[CatalogItem] = []  

    def add(self, item: CatalogItem):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("  (catalog is empty)")
            return
        for item in self.items:         
            print(" ", item)




def load_catalog(path: str, catalog: Catalog) -> None:
    """Read title|year|kind lines and populate catalog. Silent on missing file."""
    try:                                
        with open(path, encoding="utf-8") as f:   
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 3:
                    continue            
                title, year_str, kind = parts
                catalog.add(CatalogItem(title=title, year=int(year_str), kind=kind))
    except FileNotFoundError:           
        pass                            


def save_catalog(path: str, catalog: Catalog) -> None:
    """Write catalog items back in title|year|kind format."""
    with open(path, "w", encoding="utf-8") as f:  
        for item in catalog.items:       
            f.write(f"{item.title}|{item.year}|{item.kind}\n")


def main() -> None:
    print("# My catalog — movies")      

    catalog = Catalog()
    load_catalog(DATA_FILE, catalog)

    while True:                         
        print("\n1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ").strip()  

        if choice == "1":              
            title = input("Title: ").strip()
            year_raw = input("Year: ").strip()
            kind = input("Genre: ").strip()

            try:
                year = int(year_raw)
            except ValueError:
                print("  Year must be a number — item not added.")
                continue

            catalog.add(CatalogItem(title=title, year=year, kind=kind))
            print(f"  Added: {catalog.items[-1]}")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(DATA_FILE, catalog)
            print("  Saved.")

        elif choice == "4":
            save_catalog(DATA_FILE, catalog)
            print("Saved. Bye!")
            break                       

        else:
            print("  Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()