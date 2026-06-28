
# magacaygu waa muna

def load_notes(myfile):
    try:
        with open(myfile, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []
print(load_notes("note.txt"))


def save_notes(myfile, notes):
    with open(myfile, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    notes = load_notes("notes.txt")

    name = input("Enter your name: ")
    print("Welcome", name)

    while True:
        print("\n1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)

        elif choice == "2":
            if len(notes) == 0:
                print("No notes yet.")
            else:
                for n in notes:
                    print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice, try again.")
