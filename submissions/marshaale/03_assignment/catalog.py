# Marshaale

#
# This program is simple game catalog program.
# allows users to add games or retrieve games
#

from dataclasses import dataclass

@dataclass
class Game:
    name:str
    year:str
    platform:str # pc, playstation, xbox, nintendo, mobile

    def __str__(self):
        return f"name: {self.name} \nyear: {self.year} \nplatform: {self.platform}\n"

class Catalog:
    def __init__(self):
        self.items = []
    
    def add(self,catalog):
        self.items.append(catalog)

    def list_all(self):
        for item in self.items:
            print(item)    


def load_catalog(path, catalog):
    try:
        with open(path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                name, year, platform = line.strip().split('|')
                game = Game(name, year, platform)
                catalog.add(game)
    except FileNotFoundError:
        print(f"File {path} does not exists")

def save_catalog(path, catalog):
    with open(path,'w',encoding='utf-8') as f:
        for item in catalog.items:
            f.write(f"{item.name}|{item.year}|{item.platform}\n")

def main():
    file_path = "catalog.txt"
    game_catalog = Catalog()
    load_catalog(file_path, game_catalog)

    while True:
        print("\n---Game Catalog---")
        print("1) Add  2) List  3) Save  4) Quit")
        user_pick = input("Pick: ")

        if user_pick == "1":
            name = input("Name: ")
            year = input("Year: ")
            platform = input("Platform: ")

            if name == "" or year == "" or platform == "":
                print("All fields are required.")
                continue

            if platform not in ["pc", "playstation", "xbox", "nintendo", "mobile"]:
                print("Invalid platform. Must be one of: pc, playstation, xbox, nintendo, mobile.")
                continue
            
            game = Game(name, year, platform)
            game_catalog.add(game)
        elif user_pick == "2":
            game_catalog.list_all()
        elif user_pick == "3":
            save_catalog(file_path,game_catalog)
            print("Saved.")
        elif user_pick == "4":
            save_catalog(file_path,game_catalog)
            print("Saved. Bye!")
            break
        else:
            print("invalid number picked")


if __name__ == "__main__":
    main()