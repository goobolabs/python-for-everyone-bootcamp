# Magaca: Abdirahman
# Shaqada: Study Log - Barnaamij lagu diiwaangeliyo waxa aad baratay maalin kasta

def load_geeyd(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print("Fayl hore lama helin, buug cusub ayaa bilaabanaya.")
        return []


def save_geeyd(path, geeyd):
    with open(path, "w", encoding="utf-8") as f:
        for item in geeyd:
            f.write(item + "\n")


def show_menu():
    print("\n========== MENU ==========")
    print("1) Add new note")
    print("2) Show geeyd")
    print("3) Quit & Save")
    print("==========================")

def main():
    file_path = "geeyd.txt"
    geeyd = load_geeyd(file_path)

    name = input("Magacaaga geli: ")
    print(f"\nHello {name}, let's track your learning! ")

    while True:
        show_menu()
        choice = input("Dooro option: ").strip()

        if choice == "1":
            note = input("Maxaad maanta baratay? ").strip()
            
            if note == "":
                print("Qoraal madhan lama ogola!")
            else:
                geeyd.append(note)
                print(" Note waa la kaydiyay (temporary).")

        elif choice == "2":
            print("\n Study geeyd:")
            if len(geeyd) == 0:
                print("Wali wax ma qorin.")
            else:
                for i, note in enumerate(geeyd, 1):
                    print(f"{i}. {note}")

        elif choice == "3":
            save_geeyd(file_path, geeyd)
            print(f" Waa la kaydiyay. Nabad gelyo {name}!")
            break

        else:
            print(" Doorasho khaldan. Fadlan isku day mar kale.")


if __name__ == "__main__":
    main()