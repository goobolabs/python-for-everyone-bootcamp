# i am TheShakirr my project is  Music Catalog: manage your music collection from the terminal

from dataclasses import dataclass

@dataclass 
class CatalogItem:
    title: str
    artist: str
    year: int

    def __str__(self):
        return f"{self.title} {self.artist} ({self.year})"
    
class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        for item in self.items:
            print(item)


def load_catalog(path , catalog):
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(" | ")
                item = CatalogItem(parts[0], parts[1], int(parts[2]))
                catalog.items.append(item)
    except FileNotFoundError:
        pass



def save_catalog(path,catalog):
    with open(path, "w" , encoding= 'utf-8') as f:
        for item in catalog.items:
            f.write(f"{item.title} | {item.artist} | {item.year}\n")




def main():
    path = "music.txt"
    catalog= Catalog()
    load_catalog(path, catalog)


    while True:
        print("1. Add ")
        print("2. List ")
        print("3. save ")
        print("4. quit")

        choice = input("choose an option: ")

        if choice == "1":
            title = input("title: ")
            artist = input("artist: ")
            year = int(input("year: "))
            catalog.add_item(CatalogItem(title, artist, year))


        elif choice == "2":
            catalog.list_all()

        elif choice == "3":
            save_catalog(path, catalog)
            print("saved.")
        elif choice == "4":
            save_catalog(path, catalog)
            print("saved, goodbye.")
            break

        else:
            print("invalid option, try again.")
            

main()
