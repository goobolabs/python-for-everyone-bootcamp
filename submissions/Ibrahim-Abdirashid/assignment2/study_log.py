# Magaca: Ibrahim Abdirashid
# Shaqada: Barnaamij fudud oo lagu kaydiyo qoraallada waxbarashada (Study Log)

def load_notes(path):
    """Waxay ka soo raddaysaa qoraallada faylka notes.txt"""
    notes = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                notes.append(line.strip())
    except FileNotFoundError:
        return []
    return notes

def save_notes(path, notes):
    """Waxay ku kaydinaysaa dhammaan qoraallada faylka notes.txt"""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(f"{note}\n")

def main():
    file_name = "notes.txt"
    
    notes = load_notes(file_name)
    
    user_name = input("Fadlan qor magacaaga: ")
    print(f"\nKu soo dhowaad {user_name}, kani waa Buug-yarahaaga Waxbarashada!")

    while True:
        print("\n--- MENU ---")
        print("1) Add a note (Ku dar qoraal)")
        print("2) List all notes (Tus dhammaan)")
        print("3) Save and Quit (Kaydi oo ka bax)")
        
        choice = input("Dooro (1, 2, ama 3): ")

        if choice == "1":
            new_note = input("Qor waxaad baratay: ")
            notes.append(new_note)
            print("Waa la xaqiijiyay!")

        elif choice == "2":
            print("\nQoraalladaada:")
            if not notes:
                print("- Buuggaagu hadda waa maran yahay.")
            else:
                for n in notes:
                    print(f"- {n}")

        elif choice == "3":
            save_notes(file_name, notes)
            print(f"Macasalaama {user_name}! Xogtaada waa la kaydiyay.")
            break 

        else:
            print("Error: Fadlan dooro mid ka mid ah lambarada kor ku qoran.")


if __name__ == "__main__":
    main()