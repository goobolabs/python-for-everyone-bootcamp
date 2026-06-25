
# mrfiiqane == so dhowow magacaygu waa mohamed mohamud Kani waa assignment 3  ==
from dataclasses import dataclass
from pathlib import Path
BASE_DIR = Path(__file__).parent

catalog_file = BASE_DIR / "catalog.txt"

@dataclass
class CatalogItem():
  title: str
  year: int

  def __str__(self):
    return f"{self.title}, {self.year}"
  

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("No books found.")
            return

        print("\n Book Catalog:")

        for item in self.items:
            print("-", item)

# soo jiido notes ka 
def load(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as f:
            items = []
            for line in catalog.items:
                line = line.strip()
                if not line:
                    continue

                title, year = line.split("|")
                items.append(CatalogItem(title, int(year)))

            return items

    except FileNotFoundError:
        print("file not found")
        return []

# save garee 
def save(path, catalog):
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}\n")


def main():

    catalog = Catalog()

    load(catalog_file, catalog)

    print("Welcome to  Book Catalog")

    while True:

        print("\n1. Add Book, \n2. List Books, \n3. Save \n4. Quit")
    
        choice = input("choice: ")

        if choice == "1":

            title = input("Title: ")
            year = int(input("Year: "))

            item = CatalogItem(title, year)
            catalog.add_item(item)

            print("Book added!")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":

            save(catalog_file, catalog)
            print("Catalog saved!")

        elif choice == "4":
            save(catalog_file, catalog)
            print("Saved. Bye!")
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
