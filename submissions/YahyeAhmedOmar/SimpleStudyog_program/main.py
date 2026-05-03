# Yahye Ahmed
# Simple study log program that saves and loads notes using files

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        notes = []

        for line in lines:
            notes.append(line.strip())

        return notes

    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes("notes.txt")

    name = input("Enter your name: ")
    print("Welcome,", name + "!")

    while True:
        print()
        print("1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note added!")

        elif choice == "2":
            print("Your Notes:")

            if len(notes) == 0:
                print("No notes found.")
            else:
                for note in notes:
                    print("-", note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()