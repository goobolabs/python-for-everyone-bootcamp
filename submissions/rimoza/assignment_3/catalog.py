# Ridwan Mohamed Abdi - 11/05/2026 (rimoza)
# A small personal book catalog. The user can add a book, list all books,
# save them to a file, and quit. Books are loaded from the file on start.

from dataclasses import dataclass, field


@dataclass
class CatalogItem:
    title: str
    author: str

    def __str__(self):
        return self.title + " by " + self.author


@dataclass
class Catalog:
    items: list = field(default_factory=list)

    def add(self, item):
        self.items.append(item)

    def list_all(self):
        if len(self.items) == 0:
            print("No books yet.")
            return
        for item in self.items:
            print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n")
                if line == "":
                    continue
                parts = line.split("|")
                if len(parts) == 2:
                    catalog.add(CatalogItem(title=parts[0], author=parts[1]))
    except FileNotFoundError:
        return


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(item.title + "|" + item.author + "\n")


def main():
    path = "books.txt"
    catalog = Catalog()
    load_catalog(path, catalog)

    print("My catalog - books")

    while True:
        print("\n1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            catalog.add(CatalogItem(title=title, author=author))
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
            print("Please pick 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
