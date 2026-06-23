# Kifah Abdi# Kifah14
# Simple money catalog program using dates and amounts

from dataclasses import dataclass


@dataclass
class CatalogItem:
    taariikh: str
    lacag: int

    def __str__(self):
        return f"Taariikh: {self.taariikh} - Lacag: ${self.lacag}"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
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
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) == 2:
                    taariikh = parts[0]
                    lacag = int(parts[1])

                    item = CatalogItem(taariikh, lacag)
                    catalog.add_item(item)

    except FileNotFoundError:
        print("No catalog file found. Starting empty.")


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.taariikh}|{item.lacag}\n")


def main():
    catalog = Catalog()
    file_path = "catalog.txt"

    load_catalog(file_path, catalog)

    while True:
        print("\nMoney Catalog")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            taariikh = input("Taariikh: ")

            try:
                lacag = int(input("Lacag: "))

                item = CatalogItem(taariikh, lacag)
                catalog.add_item(item)

                print("Item added.")

            except ValueError:
                print("Lacagtu waa inay number noqotaa.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(file_path, catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
# Simple money catalog program using dates and amounts

from dataclasses import dataclass


@dataclass
class CatalogItem:
    taariikh: str
    lacag: int

    def __str__(self):
        return f"Taariikh: {self.taariikh} - Lacag: ${self.lacag}"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
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
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) == 2:
                    taariikh = parts[0]
                    lacag = int(parts[1])

                    item = CatalogItem(taariikh, lacag)
                    catalog.add_item(item)

    except FileNotFoundError:
        print("No catalog file found. Starting empty.")


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.taariikh}|{item.lacag}\n")


def main():
    catalog = Catalog()
    file_path = "catalog.txt"

    load_catalog(file_path, catalog)

    while True:
        print("\nMoney Catalog")
        print("1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        if choice == "1":
            taariikh = input("Taariikh: ")

            try:
                lacag = int(input("Lacag: "))

                item = CatalogItem(taariikh, lacag)
                catalog.add_item(item)

                print("Item added.")

            except ValueError:
                print("Lacagtu waa inay number noqotaa.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(file_path, catalog)
            print("Catalog saved.")

        elif choice == "4":
            save_catalog(file_path, catalog)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()