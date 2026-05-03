
NOTES_FILE = "notes.txt"


def load_notes(path):
    """Load notes from a file and return a list of stripped lines."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Save notes to a file, one note per line."""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes(NOTES_FILE)
    print("Welcome to the study log.")
    name = input("What is your name? ").strip()
    if name:
        print(f"Hello, {name}! You can add notes, list notes, or quit.")
    else:
        print("Hello! You can add notes, list notes, or quit.")

    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            note = input("Note: ").strip()
            if note:
                notes.append(note)
                print("Note added.")
            else:
                print("No note entered.")
        elif choice == "2":
            if notes:
                print("\nYour notes:")
                for note in notes:
                    print(note)
            else:
                print("No notes yet.")
        elif choice == "3":
            save_notes(NOTES_FILE, notes)
            print("Bye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
