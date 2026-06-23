# Fatima Mohamed Omar
# Barnaamij fudud oo kaydiya, akhriya, kuna soo bandhiga xogta catalog-ka.

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

    def add(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("Catalog-ku waa madhan yahay.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    title = parts[0]
                    year = int(parts[1])

                    item = CatalogItem(title, year)
                    catalog.add(item)

    except FileNotFoundError:
        pass


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    path = "catalog.txt"

    catalog = Catalog()
    load_catalog(path, catalog)

    while True:
        print("\nMenu")
        print("1 = Ku dar item")
        print("2 = Muuji items")
        print("3 = Save garee")
        print("4 = Ka bax")

        choice = input("Dooro: ")

        if choice == "1":
            title = input("Geli title-ka: ")
            year = int(input("Geli sanadka: "))

            item = CatalogItem(title, year)
            catalog.add(item)

            print("Item-ka waa lagu daray.")

        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)
            print("Catalog-ka waa la save gareeyay.")

        elif choice == "4":
            save_catalog(path, catalog)
            print("Nabad gelyo.")
            break

        else:
            print("Doorasho khaldan.")


main()