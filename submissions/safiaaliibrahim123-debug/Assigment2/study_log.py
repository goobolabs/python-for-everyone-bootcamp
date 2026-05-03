# Name:safiya
# Program: Simple Study Log - kaydi oo soo bandhig qoraalada waxbarasho

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes("notes.txt")

    name = input("Magacaaga geli: ")
    print(f"Soo dhawoow {name}!\n")

    while True:
        print("1) Add note  2) List  3) Quit")
        choice = input("Dooro: ")

        if choice == "1":
            note = input("Qor note: ")
            notes.append(note)

        elif choice == "2":
            print("\nNotes-kaaga:")
            for note in notes:
                print(note)
            print()

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Fadlan dooro 1, 2, ama 3\n")


if __name__ == "__main__":
    main()
