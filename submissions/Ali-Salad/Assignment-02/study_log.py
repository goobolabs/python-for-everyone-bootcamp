# Student: Ali-Salad
# Description: A simple study log that lets you add and list notes,
#              saved to a text file so they persist between sessions.

FILE_PATH = "notes.txt"


def load_notes(path):
    """Read notes from file and return them as a list of strings.
    Returns an empty list if the file does not exist yet."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            notes = [line.rstrip("\n") for line in f]
        return notes
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Write every note in the list to the file, one per line."""
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    # --- Greeting (optional stretch from Assignment 1) ---
    name = input("What is your name? ").strip()
    print("Welcome, " + name + "! Let's log your study notes.\n")

    # --- Load existing notes from file ---
    notes = load_notes(FILE_PATH)

    if notes:
        print("Loaded " + str(len(notes)) + " saved note(s).\n")
    else:
        print("No saved notes found. Starting fresh.\n")

    # --- Menu loop ---
    while True:
        print("1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            note = input("Note: ").strip()
            if note:                        # only add non-empty notes
                notes.append(note)
                print("Note saved!\n")
            else:
                print("Empty note skipped.\n")

        elif choice == "2":
            if notes:
                print("\n--- Your notes ---")
                for i, note in enumerate(notes, start=1):
                    print(str(i) + ". " + note)
                print()
            else:
                print("No notes yet. Add one first!\n")

        elif choice == "3":
            save_notes(FILE_PATH, notes)
            print("Bye, " + name + "! Notes saved.")
            break                           # exit the loop

        else:
            print("Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
