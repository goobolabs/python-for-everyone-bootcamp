# Name: Mukhtar-kaariye
# Program: Simple movie catalog that allows users to add, list, save, and load movies

from dataclasses import dataclass


# Movie item
@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"


# Catalog class
class Catalog:

    def __init__(self):
        self.items = []

    # Add movie
    def add_item(self, item):
        self.items.append(item)

    # List movies
    def list_all(self):

        if len(self.items) == 0:
            print("No movies in catalog.")

        else:
            print("\nMovie Catalog:")

            for item in self.items:
                print(item)


# Load movies from file
def load_catalog(path, catalog):

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line in file:

                parts = line.strip().split("|")

                if len(parts) == 2:

                    title = parts[0]
                    year = int(parts[1])

                    movie = CatalogItem(title, year)

                    catalog.add_item(movie)

    except FileNotFoundError:
        print("No saved catalog found. Starting new catalog.")


# Save movies to file
def save_catalog(path, catalog):

    with open(path, "w", encoding="utf-8") as file:

        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


# Main program
def main():

    print("My Movie Catalog")

    catalog = Catalog()

    # Load saved data
    load_catalog("catalog.txt", catalog)

    while True:

        print("\n1) Add")
        print("2) List")
        print("3) Save")
        print("4) Quit")

        choice = input("Pick: ")

        # Add movie
        if choice == "1":

            title = input("Title: ")
            year = input("Year: ")

            # Check if year is a number
            if year.isdigit():

                movie = CatalogItem(title, int(year))

                catalog.add_item(movie)

                print("Movie added!")

            else:
                print("Year must be a number.")

        # List movies
        elif choice == "2":

            catalog.list_all()

        # Save catalog
        elif choice == "3":

            save_catalog("catalog.txt", catalog)

            print("Catalog saved!")

        # Quit
        elif choice == "4":

            save_catalog("catalog.txt", catalog)

            print("Saved. Bye!")
            break

        # Invalid option
        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()