# #Hodon maxamed
# #Build a tiny catalog (movies, games, or books—your pick).

from dataclasses import dataclass
@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title}, ({self.year})"



def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [s.strip().split() for s in f]
        


    except FileNotFoundError:
        print("file errorr")


#saving catalog
def save_catalog(path, catalog):
    try:
        with open(path, "w", encoding="utf-8") as file:
            for item in catalog.items:
                file.write(f"{item.title}|{item.year} \n ")


    except FileNotFoundError:
      print("file error")    



class Catalog:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item) 
    def list_all(self):
        if not self.items:
            print("no lists yet ") 
        else:
            for item in self.items:
                print(item)          
    

#main def

def main():
    path = "catalog.txt"

    catalog = Catalog()
    load_catalog(path, catalog)

    print("my catalog movies ")

    while True:
        print("1)Add, 2)List, 3)save, 4)quit ")
        pick = input("pick: ")
        if pick == "1":
            title = input("title: ")
            year = input("year: ")
            item = CatalogItem(title, year)
            catalog.add(item)

        elif pick == "2":
            catalog.list_all()    
        elif pick == "3":
            save_catalog(path, catalog)
            print("saved")
        elif pick == "4":
            save_catalog(path, catalog)
            print("saved. bye") 
            break   

        else:
            print("valid number")


if __name__ == "__main__":
    main()


