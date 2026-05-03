# Name: Abdullahi Abdisamed nur
# Program: A simple study log that lets the user add notes, view them,
# and saves/loads notes from a file.

def load_notes(path):
    """Load notes from a file and return as a list of strings."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Save a list of notes to a file."""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    print("Welcome to Study Log!")

    # Optional: ask for name
    name = input("What is your name? ")
    print(f"Hello, {name}!")

    notes = load_notes("notes.txt")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            new_note = input("Note: ")
            notes.append(new_note)

        elif choice == "2":
            print("\nYour notes:")
            for note in notes:
                print(note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")


if __name__ == "__main__":
    main()
