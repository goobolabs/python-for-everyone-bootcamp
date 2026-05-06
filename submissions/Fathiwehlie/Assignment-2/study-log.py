# study_log.py

FILE_NAME = "notes.txt"
name = input("Enter your name: ")
def load_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes()

    while True:

        print("1 = Add note")
        print("2 = List notes")
        print("3 = Quit")

       
        pick = input(f"\nHello {name}, welcome to your Study Log \nPlease pick an option (1/2/3): ")
        if pick == "1":
            note = input("Enter your note: ")
            notes.append(note)
            save_notes(notes)
            print("Note saved!")

        elif pick == "2":
            print("\n--- Your Notes ---")
            if len(notes) == 0:
                print("No notes yet.")
            else:
                for note in notes:
                    print("-", note)

        elif pick == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()