

NOTES_FILE = "my_notes.txt"  # Magac cusub


def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        f.writelines(note + "\n" for note in notes)  # writelines bedel for-loop


def add_note(notes):
    note = input("Write your note: ").strip()  # .strip() cusub
    if not note:
        print("Empty note ignored.")
        return
    notes.append(note)
    print("Note saved!")


def list_notes(notes):
    if not notes:
        print("No notes found.")
        return
    print("\n--- Your Notes ---")  # Header kala duwan
    for i, note in enumerate(notes, 1):
        print(f"  {i}. {note}")


def delete_note(notes):
    if not notes:
        print("Nothing to delete.")
        return

    list_notes(notes)
    try:
        num = int(input("Note number to delete: "))
        if 1 <= num <= len(notes):
            removed = notes.pop(num - 1)
            print(f'Removed: "{removed}"')
        else:
            print("Number out of range.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    notes = load_notes()

    name = input("Your name: ").strip()  # .strip() cusub
    print(f"\nHey {name}, welcome back! 👋")  # Ereyada kala duwan

    menu = "\nOptions: 1) Add  2) View  3) Delete  4) Quit"  # Variable u ah menu

    while True:
        print(menu)
        choice = input("Choice: ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            save_notes(notes)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if name == "main":  # Bug fix: name → name
    main()