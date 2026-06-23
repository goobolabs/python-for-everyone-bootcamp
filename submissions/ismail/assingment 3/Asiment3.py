# Ismail Nouh Hudhuun
# Simple personal movie catalog program using classes, files, and menus.

from dataclasses import dataclass


@dataclass
class CatalogItem:
    full_name: str
    brith_year: int

    def __str__(self):
        return f"{self.full_name} ({self.brith_year})"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("Catalog is empty.")
            return

        print("\nMovie Catalog:")
        for item in self.items:
            print(item)

    def save_catalog(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for item in self.items:
                file.write(f"{item.full_name}|{item.brith_year}\n")

    def load_catalog(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split("|")

                    if len(parts) == 2:
                        full_name = parts[0]
                        brith_year = int(parts[1])

                        item = CatalogItem(full_name, brith_year)
                        self.add_item(item)

        except FileNotFoundError:
            pass

        except ValueError:
            print("Invalid data in catalog file.")
            self.items = []

        except Exception as e:
            print(f"Error loading catalog: {e}")
            self.items = []

        finally:
            pass

    def __str__(self):
        return "My Catalog"


catalog = Catalog()
catalog.load_catalog("catalog.txt")
catalog.list_all()

while True:
    print("\nMy Catalog — Movies")
    print("1) Add")
    print("2) List")
    print("3) Save")
    print("4) Quit")

    choice = input("Pick: ")

    if choice == "1":
        full_name = input("Full Name: ")

        brith_year_input = input("Brith Year: ")

        try:
            brith_year = int(brith_year_input)

            item = CatalogItem(full_name, brith_year)
            catalog.add_item(item)

            print("Movie added.")

        except ValueError:
            print("Brith Year must be a number.")

    elif choice == "2":
        catalog.list_all()

    elif choice == "3":
        catalog.save_catalog("catalog.txt")
        print("Catalog saved.")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice. Try again.")

    print()



