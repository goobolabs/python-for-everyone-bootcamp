# Mohamed Hassan
# Program-kan waa catalog yar oo lagu kaydiyo xogta beeraha.

from dataclasses import dataclass


@dataclass
class CatalogItem:
    magaca_beerta: str
    nooca_dalagga: str

    def __str__(self):
        return f"Beer: {self.magaca_beerta} | Dalag: {self.nooca_dalagga}"


class Catalog:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):

        if len(self.items) == 0:
            print("Wax beer ah lama helin.\n")

        else:
            print("\n--- Liiska Beeraha ---")

            for item in self.items:
                print(item)

            print()


def load_catalog(path, catalog):

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line in file:

                data = line.strip().split("|")

                if len(data) == 2:

                    magaca_beerta = data[0]
                    nooca_dalagga = data[1]

                    item = CatalogItem(magaca_beerta, nooca_dalagga)

                    catalog.add_item(item)

    except FileNotFoundError:
        pass


def save_catalog(path, catalog):

    with open(path, "w", encoding="utf-8") as file:

        for item in catalog.items:

            file.write(f"{item.magaca_beerta}|{item.nooca_dalagga}\n")


def main():

    file_name = "beeraha.txt"

    catalog = Catalog()

    load_catalog(file_name, catalog)

    print("=== Beeraha Catalog System ===")

    while True:

        print("1. Ku dar beer")
        print("2. Arag beeraha")
        print("3. Save")
        print("4. Quit")

        choice = input("Dooro option: ")

        if choice == "1":

            magaca_beerta = input("Geli magaca beerta: ")

            nooca_dalagga = input("Geli nooca dalagga: ")

            new_item = CatalogItem(magaca_beerta, nooca_dalagga)

            catalog.add_item(new_item)

            print("Beerta waa lagu daray.\n")

        elif choice == "2":

            catalog.list_all()

        elif choice == "3":

            save_catalog(file_name, catalog)

            print("Catalog-ga waa la kaydiyay.\n")

        elif choice == "4":

            save_catalog(file_name, catalog)

            print("Xogta waa la kaydiyay. Nabad gelyo!")

            break

        else:
            print("Doorasho khaldan.\n")


if __name__ == "__main__":
    main()
