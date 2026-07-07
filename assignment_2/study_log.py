# Name: Ridwan Muuse (or your alias)
# Program: study_log.py
# Description: A simple study log program that lets the user add notes,
# view them, and save/load from a file.

def load_notes(path):
    """Load notes from a file. Return a list of lines."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Save notes to a file, one per line."""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    # Optional: ask user name
    name = input("Enter your name: ")
    print(f"Welcome, {name}! 📘")

    notes = load_notes("notes.txt")

    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)

        elif choice == "2":
            print("\nYour notes:")
            for n in notes:
                print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Try 1, 2, or 3.")


if __name__ == "__main__":
    main()