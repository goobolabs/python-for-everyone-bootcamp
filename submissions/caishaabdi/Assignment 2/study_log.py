# Name: Aisha Abdullahi Mohamed  \gitUser: caishaabdi
# Description: Simple study log program that saves and loads notes from a file
# Assignment 2: Simple study log

def load_notes(path):
    """Load notes from a file. If file doesn't exist, return empty list"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            notes = f.readlines()
            return [note.strip() for note in notes]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Save all notes to a file."""
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    file_path = "notes.txt"
    notes = load_notes(file_path)

    print("Welcome to Simple Study Log!")

    while True:
        print("\nMenu:")
        print("1 - Add note")
        print("2 - List notes")
        print("3 - Quit")

        choiceOption = input("Choose an option: ")

        if choiceOption == "1":
            new_note = input("Write your note: ")
            notes.append(new_note)
            print("Note added!")

        elif choiceOption == "2":
            print("\nYour Notes:")
            if len(notes) == 0:
                print("No notes yet.")
            else:
                for i, note in enumerate(notes, start=1):
                    print(str(i) + ". " + note)

        elif choiceOption == "3":
            save_notes(file_path, notes)
            print("Notes saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again")


if __name__ == "__main__":
    main()