# Name: Abdullaahi maxamed axmed
# Program: Simple Study Log - allows user to add, view, and save notes

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
    print("Welcome,", name)

    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
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
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()