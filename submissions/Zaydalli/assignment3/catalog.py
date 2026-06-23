# Name: Zaydalli
# Description: A personal catalog program to manage a list of favorite movies, utilizing OOP and file handling.

from dataclasses import dataclass

@dataclass
class CatalogItem:
    title: str
    year: str
    
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

def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip("\n")
                if line:

                    parts = line.split("|")
                    if len(parts) >= 2:
                        title = parts[0]
                        year = parts[1]
                        item = CatalogItem(title=title, year=year)
                        catalog.add(item)
    except FileNotFoundError:
        pass 

def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")

def main():
    print("My catalog — movies")
    catalog = Catalog()
    file_path = "catalog.txt"
    
    load_catalog(file_path, catalog)
    
    while True:
        print("\n1) Add  2) List  3) Save  4) Quit")
        pick = input("Pick: ")
        
        if pick == "1":
            title = input("Title: ")
            year = input("Year: ")
            item = CatalogItem(title=title, year=year)
            catalog.add(item)
        elif pick == "2":
            catalog.list_all()
        elif pick == "3":
            save_catalog(file_path, catalog)
            print("Saved.")
        elif pick == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break
        else:
            print("Invalid option. Please pick 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
