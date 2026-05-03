

FILENAME = "notes.txt"


def load_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def add_note(notes):
    note = input("Note: ")
    notes.append(note)
    print("Saved!")


def list_notes(notes):
    if not notes:
        print("No notes yet.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")


def delete_note(notes):
    if not notes:
        print("Nothing to delete.")
        return

    list_notes(notes)
    try:
        num = int(input("Delete note number: "))
        if 1 <= num <= len(notes):
            removed = notes.pop(num - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number!")


def main():
    notes = load_notes()

    name = input("Enter your name: ")
    print(f"Welcome {name} 👋")

    while True:
        print("\n1) Add note  2) List  3) Delete  4) Quit")
        choice = input("Pick: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            list_notes(notes)

        elif choice == "3":
            delete_note(notes)

        elif choice == "4":
            save_notes(notes)
            print("Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()