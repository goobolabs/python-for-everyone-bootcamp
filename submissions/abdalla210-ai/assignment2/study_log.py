# Author: Clear
# Program: Simple notes app that loads notes from a file
#lets the user add/list notes, and saves on quit.

def load_notes(filename):
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_notes(filename, notes):
    """Save notes to a file."""
    with open(filename, "w") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    filename = "notes.txt"
    notes = load_notes(filename)

    while True:
        print("\n1: Add")
        print("2: List")
        print("3: Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_cusub = input("Enter your note: ")
            notes.append(file_cusub)
            print("Note added....")

        elif choice == "2":
            print("\n--- Notes ---")
            if not notes:
                print("No notes.")
            else:
                for note in notes:
                    print(note)

        elif choice == "3":
            save_notes(filename, notes)
            print(" Goodbye....")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
