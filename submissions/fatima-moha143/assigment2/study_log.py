# Magac: Fatima Mohamed omar assigment 2


def load_notes(filename):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_notes(filename, notes):
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    # Start: load notes kahor menu
    notes = load_notes("notes.txt")

    while True:
        # Menu
        print("\n1 = Ku dar  2 = Arag  3 = Bax")
        choice = input("Dooro: ")

        # Add
        if choice == "1":
            note = input("Qor note: ")
            notes.append(note)

        # List
        elif choice == "2":
            for n in notes:
                print(n)

        # Quit
        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Nabad gelyo!")
            break

        # Else (invalid)
        else:
            print("Doorasho khaldan")


if __name__ == "__main__":
    main()