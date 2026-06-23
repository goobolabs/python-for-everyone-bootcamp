# Ridwan Mohamed Abdi - 02/05/2026 (rimoza)
# Simple study log: add short notes, list them, and save them to a file
# so they are still there next time the program runs.


def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    name = input("Please enter your name: ")
    print("Hello, " + name + "! Welcome to your study log.")

    notes = load_notes("notes.txt")

    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
        elif choice == "2":
            if len(notes) == 0:
                print("No notes yet.")
            else:
                for note in notes:
                    print(note)
        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye, " + name + "!")
            break
        else:
            print("Please pick 1, 2, or 3.")


if __name__ == "__main__":
    main()
