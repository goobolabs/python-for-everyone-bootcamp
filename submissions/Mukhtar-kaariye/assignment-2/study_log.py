# Name: Mukhtar-kaariye
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

    # Load saved notes
    notes = load_notes("notes.txt")

    # Ask user name
    name = input("Enter your name: ")
    print("Welcome,", name)

    # Menu loop
    while True:

        print("\n1) Add note  2) List  3) Quit")

        choice = input("Pick: ")

        # Add note
        if choice == "1":

            note = input("Note: ")
            notes.append(note)

            print("Note added!")

        # List notes
        elif choice == "2":

            if len(notes) == 0:
                print("No notes found.")

            else:
                print("\nYour notes:")

                for note in notes:
                    print("- " + note)

        # Quit program
        elif choice == "3":

            save_notes("notes.txt", notes)

            print("Bye!")
            break

        # Invalid choice
        else:
            print("Invalid choice, try again.")


# Run the program
if __name__ == "__main__":
    main()