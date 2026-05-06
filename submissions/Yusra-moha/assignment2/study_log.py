# study_log.py
# Student: Yusra
# Simple Study Log Program using files, loops, functions, and conditions


def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = file.read().splitlines()
            return notes
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    # input name and welcome user
    name = input("Enter your name: ")
    print("Welcome,", name)

    file_path = "notes.txt"
    notes = load_notes(file_path)

    # loop for user interaction
    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        # Add note
        if choice == "1":
            note = input("Enter your note: ")
            notes.append(note)
            print("Note added!")

        # List notes
        elif choice == "2":
            if len(notes) == 0:
                print("No notes yet.")
            else:
                print("\nYour Notes:")
                for note in notes:
                    print("- " + note)

        # Quit
        elif choice == "3":
            save_notes(file_path, notes)
            print("Bye!")
            break

        # Invalid input
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()