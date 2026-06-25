# Magaca:  Asmo Abdulaahi
# Assegment 3:Barnaamijka xafidaada agabka supermarket-ka (Catalog).

from dataclasses import dataclass

@dataclass
class Badeeco:
    """Class-kan wuxuu xafidayaa macluumaadka hal shay oo supermarket-ka yaalla"""
    magaca: str
    nooca: str  # Tusaale: Cunto, Cabitaan, ama Nadiifis
    qiimaha: float

    def __str__(self):
        # Qaabka loo soo bandhigayo badeecada
        return f"Badeecada: {self.magaca} ({self.nooca}) - Qiimaha: ${self.qiimaha}"

class SupermarketCatalog:
    """Class-kan wuxuu maamulayaa dhamaan liiska agabka"""
    def __init__(self):
        self.alaabta = []

    def ku_dar_badeeco(self, shey):
        self.alaabta.append(shey)

    def tusi_liiska(self):
        if not self.alaabta:
            print("Catalog-ga supermarket-ka waa madan yahay hadda.")
        else:
            print("\n--- Liiska Agabka Supermarket-ka ---")
            for shey in self.alaabta:
                print(shey)

def load_catalog(path, catalog_obj):
    """Xogta ayuu ka soo akhrinayaa faylka marka barnaamijku bilowdo"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                # Waxaan u kala jabinaynaa qoraalka calaamaddo "*"
                parts = line.strip().split("*")
                if len(parts) == 3:
                    # parts[0]=magac, parts[1]=nooc, parts[2]=qiimo
                    item = Badeeco(parts[0], parts[1], float(parts[2]))
                    catalog_obj.ku_dar_badeeco(item)
    except FileNotFoundError:
        # Hadii faylka la waayo, liiska waa iska madhnaanayaa
        pass

def save_catalog(path, catalog_obj):
    """Xogta ayuu ku keydinayaa faylka marka qofku baxo"""
    with open(path, "w", encoding="utf-8") as f:
        for shey in catalog_obj.alaabta:
            # Waxaan u keydinaynaa qaab kala saaran: magac*nooc*qiimo
            f.write(f"{shey.magaca}*{shey.nooca}*{shey.qiimaha}\n")

def main():
    faylka_kaydka = "supermarket_data.txt"
    my_catalog = SupermarketCatalog()
    
    # Soo saar xogtii hore
    load_catalog(faylka_kaydka, my_catalog)
    
    print("=== Supermarket Inventory System ===")
    user_name = input("Fadlan qor magacaaga: ")
    print(f"Ku soo dhowow, {user_name}!\n")

    while True:
        print("Menu: 1) Add Item  2) List All  3) Save  4) Quit")
        choice = input("Dooro mid (1-4): ")

        if choice == "1":
            m = input("Magaca badeecada: ")
            n = input("Nooca (e.g. Cunto, Cabitaan): ")
            q = input("Qiimaha ($): ")
            # Dhisida Object-ga cusub
            item = Badeeco(m, n, float(q))
            my_catalog.ku_dar_badeeco(item)
            print("Waa la ku daray!")

        elif choice == "2":
            my_catalog.tusi_liiska()

        elif choice == "3":
            save_catalog(faylka_kaydka, my_catalog)
            print("Xogtii waa la keydiyay!")

        elif choice == "4":
            save_catalog(faylka_kaydka, my_catalog)
            print(f"Keydintii waa dhammaatay. Nabad gelyo {user_name}!")
            break
        else:
            print("Fadlan dooro lambar u dhexeeya 1 ilaa 4.")

if __name__ == "__main__":
    main()
