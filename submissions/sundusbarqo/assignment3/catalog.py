# Name: Sundus
# Assignment: A simple program to track my book collection

from dataclasses import dataclass

@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} - Published: {self.year}"

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: CatalogItem):
        self.items.append(item)

    def list_all(self):
        if len(self.items) == 0:
            print("Nothing in the catalog yet!")
        else:
            for info in self.items:
                print(info)

def load_catalog(path, catalog):
    try:
        f = open(path, "r", encoding="utf-8")
        for line in f:
            data = line.strip().split('|')
            if len(data) == 2:
                new_title = data[0]
                new_year = int(data[1])
                catalog.add_item(CatalogItem(new_title, new_year))
        f.close()
    except FileNotFoundError:
        print("No save file found, starting a new catalog.")

def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.items:
            f.write(f"{item.title}|{item.year}\n")

def main():
    filename = "catalog.txt"
    my_books = Catalog()
    
    load_catalog(filename, my_books)

    while True:
        print("\n--- BOOK CATALOG MENU ---")
        print("1) Add Book  2) List All  3) Save  4) Quit")
        
        user_choice = input("What do you want to do? ")

        if user_choice == "1":
            t = input("Enter Title: ")
            y = int(input("Enter Year: "))
            my_books.add_item(CatalogItem(t, y))
            print("Added successfully.")

        elif user_choice == "2":
            print("\nShowing all items:")
            my_books.list_all()

        elif user_choice == "3":
            save_catalog(filename, my_books)
            print("Progress saved.")

        elif user_choice == "4":
            save_catalog(filename, my_books)
            print("Saved everything. Goodbye!")
            break

        else:
            print("Not a valid option, try again.")

if __name__ == "__main__":
    main()
