# Name: hibo
# Program: Simple Study Log
# This program lets the user add notes, view notes, and saves them to a file.

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
    notes = load_notes("notes.txt")

    name = input("What is your name? ").strip()
    print(f"Welcome, {name}!")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            note = input("Note: ").strip()
            notes.append(note)

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