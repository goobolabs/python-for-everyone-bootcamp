
# Name: muse alinor

FILE = "notes.txt"


def load_notes(FILE):
  
    try:
        with open('notes.txt', "r", encoding="utf-8") as f:
            contact=f.read()
            print(contact)
         
    except FileNotFoundError:
        return []
        print("this file kaan is not exiset")

def save_notes(path, notes):
    """Write notes to file, one per line."""
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    name = input("What is your name? ")
    print(f"Welcome, {name}!")

    notes = load_notes(FILE)

    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note saved!")

        elif choice == "2":
            if notes:
                for note in notes:
                    print(note)
            else:
                print("No notes yet.")

        elif choice == "3":
            save_notes(FILE, notes)
            print(f"Bye, {name}!")
            break

        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
