# study_log.py
# Name: MUHIYADIN SAID HASSAN
# Description: A simple study log program that lets users add, view, and save notes to a file.
def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes("notes.txt")

    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note added.")

        elif choice == "2":
            if not notes:
                print("No notes yet.")
            else:
                print("\nYour notes:")
                for n in notes:
                    print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")


if __name__ == "__main__":
    main()