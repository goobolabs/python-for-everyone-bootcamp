# Name: soadmoahmud
# Program: Simple study log - save and load notes from a file

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            notes = []
            for line in lines:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


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
            for n in notes:
                print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
