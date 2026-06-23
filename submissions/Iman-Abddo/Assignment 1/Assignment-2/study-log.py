def load_notes(filename):

    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = []

            for line in f:
                notes.append(line.rstrip("\n"))

            return notes

    except FileNotFoundError:
        return []


def save_notes(filename, notes):

    with open(filename, "w", encoding="utf-8") as f:

        for note in notes:
            f.write(note + "\n")


def main():

    notes = load_notes("notes.txt")

    name = input("Enter your name: ")
    print(f"Welcome {name} 👋")

    while True:

        print("\n1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Pick: ")

        if choice == "1":

            note = input("Note: ")
            notes.append(note)
            print("Saved!")

        elif choice == "2":

            print("\nYour Notes:")

            for note in notes:
                print(note)

        elif choice == "3":

            save_notes("notes.txt", notes)

            print("Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
