# Name: Nasteho 
# Description: Program yar oo lagu qoro, lagu arko, laguna keydiyo notes (study log)

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    print("=== Study Log ===")

    # optional: magaca user
    name = input("Enter your name: ")
    print(f"Welcome, {name}!\n")

    notes = load_notes("notes.txt")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note added!")

        elif choice == "2":
            if not notes:
                print("No notes yet.")
            else:
                print("\nYour notes:")
                for note in notes:
                    print("- " + note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()