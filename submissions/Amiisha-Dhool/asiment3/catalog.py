from dataclasses import dataclass


@dataclass
class CatalogItem:
    title: str
    year: int
    genre: str

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) [{self.genre}]"


class Catalog:
    def __init__(self) -> None:
        self.items: list[CatalogItem] = []

    def add_item(self, item: CatalogItem) -> None:
        self.items.append(item)

    def list_all(self) -> None:
        if not self.items:
            print("  (catalog is empty)")
            return

        for i, item in enumerate(self.items, start=1):
            print(f"  {i}. {item}")


DATA_FILE = "catalog.txt"


def load_catalog(path: str, catalog: Catalog) -> None:
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                title, year_str, genre = parts

                try:
                    year = int(year_str)
                except ValueError:
                    continue

                catalog.add_item(
                    CatalogItem(title=title, year=year, genre=genre)
                )

    except FileNotFoundError:
        pass


def save_catalog(path: str, catalog: Catalog) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        for item in catalog.items:
            fh.write(f"{item.title}|{item.year}|{item.genre}\n")


def main() -> None:
    print("=== My Movie Catalog ===")

    catalog = Catalog()
    load_catalog(DATA_FILE, catalog)

    while True:
        print("\n1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            title = input("  Title: ").strip()
            year_str = input("  Year: ").strip()
            genre = input("  Genre: ").strip()

            try:
                year = int(year_str)
            except ValueError:
                print("  ✗ Year must be a number. Item not added.")
                continue

            if not title:
                print("  ✗ Title cannot be empty. Item not added.")
                continue

            catalog.add_item(
                CatalogItem(title=title, year=year, genre=genre)
            )

            print(f"  ✓ Added: {catalog.items[-1]}")

        elif choice == "2":
            print("── Catalog ──")
            catalog.list_all()

        elif choice == "3":
            save_catalog(DATA_FILE, catalog)
            print(f"  ✓ Saved {len(catalog.items)} item(s) to '{DATA_FILE}'.")

        elif choice == "4":
            save_catalog(DATA_FILE, catalog)
            print("Saved. Bye!")
            break

        else:
            print("  Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()